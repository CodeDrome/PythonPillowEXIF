import exif2


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Pillow EXIF   |")
    print("-----------------\n")

    try:

        filepath = "DSC_0502.jpg"

        exif_dict = exif2.generate_exif_dict(filepath)

        print_exif_dict(exif_dict)

    except IOError as ioe:

        print(ioe)


def print_exif_dict(exif_dict):

    for key, value in exif_dict.items():

        if value["raw"] is not None:
            print(key)
            print("-" * len(key))
            print(f"    tag:       {value["tag"]}")
            print(f"    raw:       {value["raw"]}")
            print(f"    processed: {value["processed"]}\n")


if __name__ == "__main__":

    main()