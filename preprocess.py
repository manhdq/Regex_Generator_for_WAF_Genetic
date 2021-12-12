import click
import json
import os
from utils import colors, makedirs


@click.command()
@click.option("--log-file", default="access.log", prompt=colors.fg.cyan+"Log file contained data", type=str)
@click.option("--type-data", default='both', prompt=colors.fg.cyan+"Get type from log [white, black, both]", type=str)
@click.option("--output-dir", default='data', prompt=colors.fg.cyan+"output dir", type=str)
def main(log_file: str, type_data: str, output_dir: str):
    assert type_data in ['white', 'black', 'both'], "type data from log must be 'white', 'black' or 'both'"
    output_file = makedirs(output_dir)

    requests_list = []
    with open(log_file) as f:
        for json_obj in f:
            request = json.loads(json_obj)
            requests_list.append(request)
    
    whitelist = []
    blacklist = []
    for req in requests_list:
        if int(req['status'].strip()) >= 400:
            print(colors.fg.red + "Denied:  \t", end='')
            blacklist.append(req['request']['request_uri'])
        else:
            print(colors.fg.green + "Accepted:\t", end='')
            whitelist.append(req['request']['request_uri'])

        print(colors.fg.lightgrey + req['status'] + '\t' + req['request']['request_uri'])

    print('\n\n' + colors.fg.cyan + f'Get {len(whitelist)} accepted data, {len(blacklist)} denied data\n')

    if type_data in ['white', 'both']:
        file = os.path.join(output_dir, 'whitelist_uri.txt')
        with open(file, 'w') as f:
            for wdata in whitelist:
                f.write(wdata + '\r\n')
            f.close()

    if type_data in ['black', 'both']:
        file = os.path.join(output_dir, 'blacklist_uri.txt')
        with open(file, 'w') as f:
            for bdata in blacklist:
                f.write(bdata + '\r\n')
            f.close()


if __name__ == '__main__':
    main()