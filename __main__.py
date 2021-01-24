import argparse

from addressline import address_converter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Analyze input address and convert it to street name and street number."
    )
    parser.add_argument(
        "--addr", type=str, help="Enter an address to convert", required=True
    )
    args = parser.parse_args()
    print(address_converter(args.addr))
