import requests


def format_bytes(size):
    # 2**10 = 1024
    power = 2 ** 10
    n = 0
    power_labels = {0: '', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return f'{size:.2f}{power_labels[n]}B'


def print_table(cuda, cudnn):
    print('| cuDNN |' + ''.join(f' CUDA{x} |' for x in cuda))
    print('| ' + '---- |' * (len(cuda) + 1))
    for i, (a, b) in enumerate(cudnn):
        print(f'| {a} |', end='')
        for c in cuda:
            url = f'https://developer.download.nvidia.com/compute/redist/cudnn/v{a}/cudnn-{c}-windows10-x64-v{b}.zip'
            filename = url[url.rfind('/')+1:]
            head = requests.head(url, allow_redirects=True)
            if head.status_code == 200:
                size = int(head.headers['Content-length'])
                print(f' [{filename}]({url}) ({format_bytes(size)}) |', end='')
            else:
                print(' - |', end='')
        print()


if __name__ == '__main__':
    cuda = ['9.0', '10.0', '10.2', '11.2', '11.3']
    cudnn = [
        ('8.2.1', '8.2.1.32'),
        ('8.1.0', '8.1.0.77'),
        ('7.4.1', '7.4.1.5'),
        ('7.2.1', '7.2.1.38'),
        ('7.1.4', '7.1'),
    ]
    print_table(cuda, cudnn)
    print()

    exit(0)

    cuda = ['9.0', '9.2', '10.0', '10.1']
    cudnn = [
        ('7.6.1', '7.6.1.34'),
        ('7.6.0', '7.6.0.64'),
        ('7.5.1', '7.5.1.10'),
        ('7.5.0', '7.5.0.56'),
        ('7.4.2', '7.4.2.24'),
        ('7.4.1', '7.4.1.5'),
        ('7.3.1', '7.3.1.20'),
        ('7.3.0', '7.3.0.29'),
        ('7.2.1', '7.2.1.38'),
        ('7.1.4', '7.1'),
    ]
    print_table(cuda, cudnn)
    print()

    cuda = ['6.5', '7.0', '7.5', '8.0', '9.0']
    cudnn = [
        ('7.2.1', '7.2.1.38'),
        ('7.1.4', '7.1'),
        ('7.1.3', '7.1'),
        ('7.1.2', '7.1'),
        ('7.0.5', '7'),
        ('7.0.4', '7'),
        ('6.0', '6.0'),
        ('5.1', '5.1'),
        ('5', '5.0-ga'),
        ('4', '4.0-prod'),
        ('3', '3.0-prod'),
        ('2', '2')
    ]
    print_table(cuda, cudnn)
