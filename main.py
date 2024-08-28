from fasthtml.common import *
from pathlib import Path

app, rt = fast_app()

def space_pascal(s): return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)

@rt("/")
def get():
    dates = sorted([d for d in Path('games').iterdir() if d.is_dir()], reverse=True)
    return Titled("Uma's Games", *[
        Div(
            H3(date.name),
            Ul(*[Li(A(f"{space_pascal(f.stem)}", href=f"/game/{date.name}/{f.stem}")) 
                for f in date.glob('*.html')])
        ) for date in dates
    ])

@rt("/game/{date}/{name}")
def get(date: str, name: str):
    f = Path(f'games/{date}/{name}.html')
    content = f.read_text()
    return Div( 
        Div(A("Back to Games", href="/"), 
            P(f"Created: {date}"), 
            Div(NotStr(content), style="border:1px solid #ccc;padding:10px;margin-top:10px;")
        )
    )

serve()