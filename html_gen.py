def generate(source: dict) -> None:
    Doc_name = source["Doc_name"]

    html_source = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{source["Title"]}</title>
</head>
<body>
    <h1>{source["h1"]}</h1>
    <p>{source["p"]}</p>
</body>
</html>
"""
    with open(f"Results/{Doc_name}.html", "w+") as file:
        file.write(html_source)

if __name__ == "__main__":
    source = dict()
    source["Doc_name"] = "index123"
    source["Title"] = "Ouffff"
    source["h1"] = "Хуййййййй"
    source["p"] = "sdnfkdsnvksnfdfv fgndflgndfklgndflk gndflgndfglkndflgndflgndfl"
    generate(source)
