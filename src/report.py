import json
import os

def save_report(results, output_path):
    """
    Saves the scan results to a JSON file.
    """
    try:
        # Ensure output directory exists
        output_dir = os.path.dirname(output_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
        
        print(f"Report saved to {output_path}")
    except Exception as e:
        print(f"Failed to save report: {e}")
