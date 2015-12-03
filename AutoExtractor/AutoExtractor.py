import argparse


def main() -> object:
    """

    :rtype: object
    """
    print("starting auto extractor")
    parser = argparse.ArgumentParser(description='Full Rar File Path.')
    parser.add_argument('filename')
    args = parser.parse_args()
    print("~ Filename: {}".format(args.filename))


"""main entry point"""
if __name__ == "__main__":
    main()
