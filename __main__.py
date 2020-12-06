from newsFinders import *
from processors import *
import json

def main():
    jFile  = open("cfg.json", "r") 
    cfg = json.load(jFile)
    finders = cfg["newsFinders"]
    processors = cfg["processors"]

    for f in finders:
        c = eval(f)()
        news = c.getData()
        if processors is not None:
            pairs = processors.items()
            for k, v in pairs:
                proc = eval(k)(c.name, news)
                if v is not None:
                    proc.execute(v)
                else:
                    proc.execute()

if __name__ == "__main__":
    main()
