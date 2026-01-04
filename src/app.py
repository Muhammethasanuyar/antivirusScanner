import argparse
import sys
import os
from .signatures import load_signatures
from .scanner import scan_directory
from .report import save_report

def main():
    parser = argparse.ArgumentParser(description="Simple Antivirus Scanner (Educational)")
    parser.add_argument("--path", required=True, help="Directory to scan")
    parser.add_argument("--out", required=True, help="Path for JSON report output")
    parser.add_argument("--signatures", default="data/signatures.json", help="Path to signature database")
    
    args = parser.parse_args()

    print(f"Starting scan on: {args.path}")
    
    # Load signatures
    if os.path.exists(args.signatures):
        print(f"Loading signatures from {args.signatures}...")
        signatures = load_signatures(args.signatures)
        print(f"Loaded {len(signatures)} signatures.")
    else:
        print("Warning: Signature file not found. Skipping signature check.")
        signatures = set()

    # Scan
    print("Scanning...")
    results = scan_directory(args.path, signatures)
    
    # Report
    save_report(results, args.out)
    
    # Summary
    detections = len(results.get("detections", []))
    print(f"\nScan Complete.")
    print(f"Total files: {results.get('total_files', 0)}")
    print(f"Detections: {detections}")
    print(f"Report saved to: {args.out}")

    if detections > 0:
        sys.exit(1) # Exit with error code if threats found
    sys.exit(0)

if __name__ == "__main__":
    main()
