import os
import shutil
import argparse
import json

class AgencyCLI:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.abspath(__file__))
        self.repo_root = os.path.join(self.base_path, "agents_data")
        self.project_root = os.getcwd()
        self.agency_dir = os.path.join(self.project_root, ".agency")
        self.agents_dir = os.path.join(self.agency_dir, "agents")

    def init(self):
        """Initializes the .agency structure in the current project."""
        if not os.path.exists(self.agency_dir):
            os.makedirs(self.agency_dir)
            os.makedirs(self.agents_dir)
            print(f"Created {self.agency_dir} directory.")
        
        # Copy templates
        templates_path = os.path.join(self.base_path, "templates")
        for template in ["project_manager.md", "prompter.md"]:
            src = os.path.join(templates_path, template)
            dst = os.path.join(self.agency_dir, template)
            shutil.copy2(src, dst)
            print(f"Provisioned {template}")

        # Initialize config
        config_path = os.path.join(self.agency_dir, "config.json")
        if not os.path.exists(config_path):
            with open(config_path, 'w') as f:
                json.dump({"installed_divisions": []}, f, indent=4)
        
        print("Initialization complete. Agency orchestrators are ready.")

    def list_divisions(self):
        """Lists available agent divisions from the source repository."""
        exclusions = {
            ".git", ".github", "agency_cli", ".agency", "scripts", 
            "integrations", "examples", "test_project", "node_modules",
            "__pycache__", "build", "dist", "test_project_all", ".agency-all"
        }
        
        if not os.path.exists(self.repo_root):
            print("Error: Agent data not found.")
            return

        divisions = [d for d in os.listdir(self.repo_root) 
                     if os.path.isdir(os.path.join(self.repo_root, d)) 
                     and d not in exclusions 
                     and not d.endswith(".egg-info")]
        
        print("Available Divisions:")
        for div in sorted(divisions):
            print(f"  - {div}")

    def create(self, division):
        """Copies agents from a specific division into the local project."""
        src_div_path = os.path.join(self.repo_root, division)
        if not os.path.exists(src_div_path):
            print(f"Error: Division '{division}' not found.")
            return

        if not os.path.exists(self.agency_dir):
            print("Error: .agency not initialized. Run 'agency init' first.")
            return

        dst_div_path = os.path.join(self.agents_dir, division)
        if not os.path.exists(dst_div_path):
            os.makedirs(dst_div_path)

        count = 0
        for item in os.listdir(src_div_path):
            if item.endswith(".md"):
                shutil.copy2(os.path.join(src_div_path, item), os.path.join(dst_div_path, item))
                count += 1
        
        # Update config
        config_path = os.path.join(self.agency_dir, "config.json")
        with open(config_path, 'r+') as f:
            config = json.load(f)
            if division not in config["installed_divisions"]:
                config["installed_divisions"].append(division)
                f.seek(0)
                json.dump(config, f, indent=4)
                f.truncate()

        print(f"Successfully installed {count} agents from '{division}' division.")

    def all_agents(self):
        """Collects ALL agents from ALL divisions into .agency-all directory."""
        all_dir = ".agency-all"
        agents_pool = os.path.join(all_dir, "agents")
        
        if not os.path.exists(all_dir):
            os.makedirs(all_dir)
            os.makedirs(agents_pool)
            print(f"Created {all_dir} directory.")

        # Copy templates to .agency-all as well
        templates_path = os.path.join(self.base_path, "templates")
        for template in ["project_manager.md", "prompter.md"]:
            src = os.path.join(templates_path, template)
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(all_dir, template))
            else:
                print(f"Warning: Template {template} not found.")

        if not os.path.exists(self.repo_root):
            print("Error: Agent data not found.")
            return

        total_count = 0
        for div in os.listdir(self.repo_root):
            div_path = os.path.join(self.repo_root, div)
            if os.path.isdir(div_path):
                for item in os.listdir(div_path):
                    if item.endswith(".md"):
                        shutil.copy2(os.path.join(div_path, item), os.path.join(agents_pool, item))
                        total_count += 1
        
        print(f"Successfully collected {total_count} agents into {all_dir}.")

def main():
    parser = argparse.ArgumentParser(description="Agency CLI - Professional AI Agent Orchestration")
    subparsers = parser.add_subparsers(dest="command", help="Commands")

    # init
    subparsers.add_parser("init", help="Initialize .agency in the current project")

    # list
    subparsers.add_parser("list", help="List available agent divisions")

    # create
    create_parser = subparsers.add_parser("create", help="Install a division of agents")
    create_parser.add_argument("--division", required=True, help="Name of the division to install")

    # all
    subparsers.add_parser("all", help="Collect all agents into .agency-all")

    args = parser.parse_args()
    cli = AgencyCLI()

    if args.command == "init":
        cli.init()
    elif args.command == "list":
        cli.list_divisions()
    elif args.command == "create":
        cli.create(args.division)
    elif args.command == "all":
        cli.all_agents()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
