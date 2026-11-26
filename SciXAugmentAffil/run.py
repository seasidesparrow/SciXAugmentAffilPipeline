import argparse
import asyncio
import os

from API import augment_server
from Augment import augment, db

def get_args():
    parser = argparse.ArgumentParser()


    subparsers = parser.add_subparsers(help="commands", dest="action")
    api_parser = subparsers.add_parser("Augment_API", help="Initialize Augment gRPC API")
    app_parser = subparsers.add_parser("Augment_APP", help="Initialize Augment Working Unit")

# APP commands
    app_parser.add_argument(
        "-l",
        "--load-all",
        dest="load_all",
        action="store_true",
        default=False,
        help="Load data from files to affil db."
    )

    return parser.parse_args()
                       

def main():

    args = get_args()

    if args.action == "Augment_APP":
        proj_home = os.path.realpath("/app/SciXAugmentAffil/")
        if args.load_all:
            augment.load_db(proj_home)
        else:
            augment.init_pipeline(proj_home)

    elif args.action == "Augment_API":
        asyncio.run(augment_server.serve())

if __name__ == "__main__":
    main()
