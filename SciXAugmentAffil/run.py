import argparse
import asyncio
import os

from API import template_server
from AugmentAffil import template

def get_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help="commands", dest="action")
    subparsers.add_parser("AugmentAffil_API", help="Initialize AugmentAffil gRPC API")
    subparsers.add_parser("AugmentAffil_APP", help="Initialize AugmentAffil Working Unit")

    parser.add_argument(
        "-l",
        "--load-all",
        dest="load_all",
        action="store_true",
        default=False,
        help="Load data from files to affil db."
    )
                       

if __name__ == "__main__":
    args = parser.parse_args()

    if args.action == "AugmentAffil_APP":
        proj_home = os.path.realpath("/app/SciXAugmentAffil/")
        template.init_pipeline(proj_home)

    elif args.action == "AugmentAffil_API":
        asyncio.run(template_server.serve())

    if args.load_all:
