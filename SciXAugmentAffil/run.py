import argparse
import asyncio
import os

from API import augment_server
from Augment import augment, db

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l",
        "--load-all",
        dest="load_all",
        action="store_true",
        default=False,
        help="Load data from files to affil db."
    )

    subparsers = parser.add_subparsers(help="commands", dest="action")
    subparsers.add_parser("Augment_API", help="Initialize Augment gRPC API")
    subparsers.add_parser("Augment_APP", help="Initialize Augment Working Unit")

    return parser.parse_args()
                       

def main():

    args = get_args()

    if args.action == "AugmentAffil_APP":
        proj_home = os.path.realpath("/app/SciXAugmentAffil/")
        augment.init_pipeline(proj_home)

    elif args.action == "AugmentAffil_API":
        asyncio.run(augment_server.serve())

    if args.load_all:
        db.load_institutions(cls)

if __name__ == "__main__":
    main()
