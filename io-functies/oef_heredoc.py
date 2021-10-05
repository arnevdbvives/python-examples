# Met Heredoc

print("""
Dit is een letterlijke tekst.
    Die wordt weergegeven zoals ik hem typ.
    \t Escaping is niet nodig.
  Zie je?
""")

# zonder heredoc
print("Dit is een letterlijke tekst.\n" + 
        "\tDie wordt weergegeven zoals ik hem typ.\n" +
        "\t Escaping is niet nodig.\n" + 
        "  Zie je?")
