from    argparse            import RawTextHelpFormatter
from    argparse            import ArgumentParser


parser  = ArgumentParser(description = "hi", formatter_class = RawTextHelpFormatter)
parser.add_argument(
    "--thingy",
    action="append",
    dest  ="thingy",
    help  ="hi",
    default = [False]
)

res = parser.parse_args()
print(res.thingy)