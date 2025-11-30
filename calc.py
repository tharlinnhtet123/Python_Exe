from __future__ import annotations

import ast
import math
import operator as op
import argparse
import sys


ALLOWED_OPERATORS = {
	ast.Add: op.add,
	ast.Sub: op.sub,
	ast.Mult: op.mul,
	ast.Div: op.truediv,
	ast.FloorDiv: op.floordiv,
	ast.Mod: op.mod,
	ast.Pow: op.pow,
}

ALLOWED_UNARY = {
	ast.UAdd: lambda x: x,
	ast.USub: lambda x: -x,
}

# whitelist math functions and constants
ALLOWED_NAMES = {k: getattr(math, k) for k in dir(math) if not k.startswith("__")}
# add some builtins
ALLOWED_NAMES.update({"abs": abs, "round": round})


def safe_eval(expr: str):
	"""Evaluate a mathematical expression safely using ast.

	Raises ValueError on invalid or unsafe expressions.
	"""
	try:
		node = ast.parse(expr, mode="eval")
	except SyntaxError as e:
		raise ValueError(f"Invalid expression: {e}")

	def _eval(n):
		if isinstance(n, ast.Expression):
			return _eval(n.body)
		if isinstance(n, ast.Constant):
			if isinstance(n.value, (int, float)):
				return n.value
			raise ValueError("Only numeric constants are allowed")
		if isinstance(n, ast.Num):  # type: ignore
			return n.n  # type: ignore
		if isinstance(n, ast.BinOp):
			op_type = type(n.op)
			if op_type in ALLOWED_OPERATORS:
				left = _eval(n.left)
				right = _eval(n.right)
				return ALLOWED_OPERATORS[op_type](left, right)
			raise ValueError(f"Operator {op_type} not allowed")
		if isinstance(n, ast.UnaryOp):
			op_type = type(n.op)
			if op_type in ALLOWED_UNARY:
				return ALLOWED_UNARY[op_type](_eval(n.operand))
			raise ValueError(f"Unary operator {op_type} not allowed")
		if isinstance(n, ast.Call):
			if isinstance(n.func, ast.Name):
				func_name = n.func.id
				if func_name in ALLOWED_NAMES:
					args = [_eval(a) for a in n.args]
					return ALLOWED_NAMES[func_name](*args)
			raise ValueError("Only direct calls to allowed functions are permitted")
		if isinstance(n, ast.Name):
			if n.id in ALLOWED_NAMES:
				val = ALLOWED_NAMES[n.id]
				if isinstance(val, (int, float)):
					return val
			raise ValueError(f"Name {n.id} is not allowed")
		raise ValueError(f"Unsupported expression: {ast.dump(n)}")

	return _eval(node)


def repl():
	print("Simple calculator. Type 'exit' or 'quit' to leave.")
	while True:
		try:
			s = input('> ').strip()
		except (EOFError, KeyboardInterrupt):
			print()
			break
		if not s:
			continue
		if s.lower() in ('exit', 'quit'):
			break
		try:
			result = safe_eval(s)
		except Exception as e:
			print(f"Error: {e}")
		else:
			print(result)


def main():
	parser = argparse.ArgumentParser(description='Safe CLI calculator')
	parser.add_argument('expr', nargs='?', help='Expression to evaluate (quotes recommended)')
	args = parser.parse_args()

	if args.expr:
		try:
			print(safe_eval(args.expr))
		except Exception as e:
			print(f"Error: {e}")
			sys.exit(1)
	else:
		repl()


if __name__ == '__main__':
	main()