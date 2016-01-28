import argparse
import crossway.QueryCrosswayESV as qCross

def get_argvparser():
    parser = argparse.ArgumentParser(description='Convert Crossway ESV Bible into SQLite')
    parser.add_argument('key', help='ESV access key (please request your ESV access key at Crossway)')
    parser.add_argument('sqlitepath', help='path of SQLite database')
    return parser

if __name__ == '__main__':
    parser = get_argvparser()
    args = parser.parse_args()

    online_parser = qCross.CrosswayOnlineESVParser(args.key)
    converter = qCross.OnlineESVToSQLiteConverter(online_parser, args.sqlitepath)
    converter.run()
    converter.closeDB()