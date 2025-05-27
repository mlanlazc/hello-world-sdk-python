from enum import Enum


class Language(Enum):
    """An enumeration representing different categories.

    :cvar EN: "en"
    :vartype EN: str
    :cvar SR: "sr"
    :vartype SR: str
    :cvar ES: "es"
    :vartype ES: str
    :cvar FR: "fr"
    :vartype FR: str
    :cvar DE: "de"
    :vartype DE: str
    :cvar NL: "nl"
    :vartype NL: str
    """

    EN = "en"
    SR = "sr"
    ES = "es"
    FR = "fr"
    DE = "de"
    NL = "nl"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, Language._member_map_.values()))
