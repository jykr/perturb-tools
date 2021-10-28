
# _print_screen_object.py
__module_name__ = "_print_screen_object.py"
__author__ = ", ".join(["Michael E. Vinyard"])
__email__ = ", ".join(["vinyard@g.harvard.edu",])


def _print_screen_object(ScreenObject):

    """
    Would be good to return an organizational dictionary
    """

    n_guides, n_conditions = ScreenObject.X.shape[0], ScreenObject.X.shape[1]

    print(
        "Genome Editing Screen comprised of n_guides x n_conditions = {} x {}\n".format(
            n_guides, n_conditions
        )
    )
    MainScreenAttributes = [
        "guides",
        "condit",
        "condit_m",
        "condit_p",
        "layers",
        "uns",
    ]

    for attribute in MainScreenAttributes:
        print("   {: <11}".format(attribute + ":"), end="")
        x = list(ScreenObject.__getattribute__(attribute).keys())
        for n, i in enumerate(x):
            if n != len(x) - 1:
                print("'{}'".format(i), end=", ")
            else:
                print("'{}'".format(i), end="")
        print("")

    return n_guides, n_conditions