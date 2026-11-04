# -*- coding: utf-8 -*-
import os

files_to_update = [
    'README.md',
    'docs/plot_concept.md',
    'docs/TEAM_COLLABORATION_SOP.md',
    'docs/WORK_LOG.md',
    'scripts/ai_video_production_script.md',
    'assets/ASSET_MANIFEST.md',
]

for rel_path in files_to_update:
    if not os.path.exists(rel_path):
        print(f"Skipping missing: {rel_path}")
        continue
    with open(rel_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace variations
    content = content.replace("《第七张罚单》（The 7th Penalty Ticket）", "《算法之外》（Beyond the Algorithm）")
    content = content.replace("《第七张罚单》", "《算法之外》")
    content = content.replace("The 7th Penalty Ticket", "Beyond the Algorithm")
    
    with open(rel_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {rel_path}")

print("All docs updated to 《算法之外》 successfully.")
