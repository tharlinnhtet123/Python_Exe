#!/usr/bin/env node
"use strict";

// Simple dice roller CLI
// Supports expressions like: 3d6+2, d20, 2d8+1d4-3, 4
// Run: node dice.js "3d6+2"  OR: node dice.js    (interactive REPL)

const readline = require("readline");

function parseAndRoll(expr) {
	if (typeof expr !== "string") throw new Error("Expression must be a string");
	expr = expr.replace(/\s+/g, "");
	if (expr.length === 0) throw new Error("Empty expression");

	const tokens = expr.match(/([+-]?\d*d\d+)|([+-]?\d+)/gi);
	if (!tokens) throw new Error("Invalid expression");

	let total = 0;
	const parts = [];

	for (const token of tokens) {
		if (token.toLowerCase().includes("d")) {
			// dice token
			const sign = token[0] === "+" ? 1 : token[0] === "-" ? -1 : 1;
			const body = token[0] === "+" || token[0] === "-" ? token.slice(1) : token;
			const [countRaw, sidesRaw] = body.split(/d/i);
			const count = countRaw === "" ? 1 : parseInt(countRaw, 10);
			const sides = sidesRaw === "%" ? 100 : parseInt(sidesRaw, 10);
			if (!Number.isFinite(count) || count < 0 || !Number.isFinite(sides) || sides <= 0) {
				throw new Error(`Invalid dice term: ${token}`);
			}

			const rolls = [];
			for (let i = 0; i < count; i++) {
				const r = Math.floor(Math.random() * sides) + 1;
				rolls.push(r);
			}
			const sum = rolls.reduce((a, b) => a + b, 0) * sign;
			total += sum;
			parts.push({type: "dice", token, sign, count, sides, rolls, sum});
		} else {
			// plain number
			const n = parseInt(token, 10);
			if (!Number.isFinite(n)) throw new Error(`Invalid number token: ${token}`);
			total += n;
			parts.push({type: "const", token, value: n});
		}
	}

	return {expr, total, parts};
}

function pretty(result) {
	const lines = [];
	lines.push(`Expression: ${result.expr}`);
	for (const p of result.parts) {
		if (p.type === "dice") {
			const signText = p.sign === -1 ? "-" : "+";
			lines.push(`${p.token}: [${p.rolls.join(", ")}] => ${signText}${Math.abs(p.sum)}`);
		} else {
			lines.push(`${p.token} => ${p.value}`);
		}
	}
	lines.push(`Total: ${result.total}`);
	return lines.join("\n");
}

function runOnce(argv) {
	const expr = argv[0];
	try {
		const res = parseAndRoll(expr);
		console.log(res.total);
		return 0;
	} catch (e) {
		console.error("Error:", e.message || e);
		return 2;
	}
}

function repl() {
	const rl = readline.createInterface({input: process.stdin, output: process.stdout, prompt: "roll> "});
	console.log("Dice roller REPL. Examples: 3d6+2, d20, 2d8+1d4-3. Type 'quit' or Ctrl+C to exit.");
	rl.prompt();
	rl.on("line", (line) => {
		const s = line.trim();
		if (!s) { rl.prompt(); return; }
		if (s.toLowerCase() === "quit" || s.toLowerCase() === "exit") { rl.close(); return; }
		try {
			const res = parseAndRoll(s);
			console.log(pretty(res));
		} catch (e) {
			console.log("Error:", e.message || e);
		}
		rl.prompt();
	}).on("close", () => {
		console.log();
		process.exit(0);
	});
}

if (require.main === module) {
	const args = process.argv.slice(2);
	if (args.length === 0) {
		repl();
	} else {
		// join args to a single expression
		const expr = args.join("");
		const code = runOnce([expr]);
		process.exit(code);
	}
}
