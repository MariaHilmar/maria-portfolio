import fs from "node:fs";
import path from "node:path";

const webRoot = process.cwd();
const targetDir = path.join(webRoot, "docs");
const sourceDir = path.join(webRoot, "..", "docs");

if (fs.existsSync(sourceDir)) {
  fs.mkdirSync(targetDir, { recursive: true });
  for (const file of fs.readdirSync(sourceDir)) {
    if (!file.endsWith(".md")) continue;
    fs.copyFileSync(path.join(sourceDir, file), path.join(targetDir, file));
  }
  console.log(`Docs sincronizados de ${sourceDir} para ${targetDir}`);
} else if (!fs.existsSync(targetDir)) {
  throw new Error(
    "Docs nao encontrados. Esperado ../docs (monorepo) ou web/docs (fallback no deploy).",
  );
} else {
  console.log(`Usando docs em ${targetDir}`);
}
