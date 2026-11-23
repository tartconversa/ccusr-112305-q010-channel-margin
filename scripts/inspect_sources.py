import argparse
import json
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / "data"


def read_table(name):
    path = DATA / f"{name}.json"
    with path.open(encoding="utf-8") as stream:
        records = json.load(stream)
    if not isinstance(records, list) or not all(isinstance(record, dict) for record in records):
        raise ValueError(f"{path.name} 应为 JSON 对象数组")
    return records


def main():
    parser = argparse.ArgumentParser(description="查看各数据来源的记录数及字段")
    parser.add_argument("source", nargs="?", help="查看单一来源，使用 JSON 文件名去掉扩展名")
    args = parser.parse_args()
    names = [args.source] if args.source else sorted(path.stem for path in DATA.glob("*.json"))
    if args.source and args.source not in {path.stem for path in DATA.glob("*.json")}:
        parser.error("未知资料来源")
    summary = {}
    for name in names:
        records = read_table(name)
        summary[name] = {"记录数": len(records), "字段": list(records[0]) if records else []}
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

