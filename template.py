import os
import shutil

# template maker script

# structure
# template/
#   ├── foo.txt
#   ├── bar/
#   │     └── baz.txt
# template.py  <- (this script)

# -----------------------------
# 🔧 Define your replacements here
# -----------------------------
replacements = [
    {
        "output": "example1",
        "mappings": {
            "pengujian-sertifikasi-pengujian-pertama-evaluator": "foo-bar",
        },
    },
    {
        "output": "example2",
        "mappings": {
            "pengujian-sertifikasi-pengujian-pertama-evaluator": "foo-bar",
        },
    },
]

# -----------------------------
# 🧠 Core logic
# -----------------------------
current_dir = os.getcwd()
template_dir = os.path.join(current_dir, "template")

if not os.path.isdir(template_dir):
    raise FileNotFoundError(f"❌ Template folder not found at: {template_dir}")

for item in replacements:
    output_name = item["output"]
    mappings = item["mappings"]
    output_dir = os.path.join(current_dir, output_name)

    # --- Remove existing output folder ---
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        print(f"[REMOVED] Existing folder: {output_dir}")

    # --- Duplicate the template folder ---
    shutil.copytree(template_dir, output_dir)
    print(f"[COPIED] Template -> {output_dir}")

    # --- Walk through all files and directories recursively ---
    for root, dirs, files in os.walk(output_dir, topdown=False):
        # ✅ Rename files
        for filename in files:
            if filename.endswith(".py"):
                continue  # skip Python files

            old_path = os.path.join(root, filename)
            new_filename = filename
            for old_str, new_str in mappings.items():
                new_filename = new_filename.replace(old_str, new_str)

            new_path = os.path.join(root, new_filename)
            if new_path != old_path:
                os.rename(old_path, new_path)
                print(f"[RENAMED FILE] {old_path} -> {new_path}")

            # --- Replace file content ---
            try:
                with open(new_path, "rb") as f:
                    if b"\0" in f.read(1024):  # skip binary files
                        continue

                try:
                    with open(new_path, "r", encoding="utf-8") as f:
                        content = f.read()
                except UnicodeDecodeError:
                    with open(new_path, "r", encoding="latin-1") as f:
                        content = f.read()

                new_content = content
                for old_str, new_str in mappings.items():
                    new_content = new_content.replace(old_str, new_str)

                if new_content != content:
                    with open(new_path, "w", encoding="utf-8") as f:
                        f.write(new_content)
                    print(f"[UPDATED CONTENT] {new_path}")

            except Exception as e:
                print(f"[ERROR] Skipping {new_path}: {e}")

        # ✅ Rename directories (bottom-up safe)
        for dirname in dirs:
            old_dir_path = os.path.join(root, dirname)
            new_dir_name = dirname
            for old_str, new_str in mappings.items():
                new_dir_name = new_dir_name.replace(old_str, new_str)
            new_dir_path = os.path.join(root, new_dir_name)
            if new_dir_path != old_dir_path:
                os.rename(old_dir_path, new_dir_path)
                print(f"[RENAMED DIR] {old_dir_path} -> {new_dir_path}")

print("\n✅ All replacements completed successfully.")
