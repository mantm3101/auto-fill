import random

comment_list = (
    'Nước ngon',
    'Được',
    'Ok',
    'Nhạc hơi to',
    'Nhạc ồn',
    'Nhạc nhỏ',
    'Nhạc hơi nhỏ',
    'Nhạc hay',
    'Nhạc hơi chập chờn',
    'Wifi yếu',
    'Nhân viên dễ thương',
    'Nhân viên nhiệt tình',
    'Quản lý nhiệt tình',
    'Trà ngon',
    'Cafe ngon',
    'Trà xanh rất ngon',
    'Quán nóng',
    'Rất tốt',
    'Ổn',
    'Nhân viên tận tình'
    'Nên giảm đồ nhựa',
    'Cafe mới rất ngon',
    'Phindi ngon',
    'Tốt',
    'Quán sạch sẽ',
    'Không',
    'Không thêm gì',
    'K',
    'Nice',
    'Nhân viên đáng yêu',
    'Ngon',
    ''
)


def random_comment():
    return random.choice(comment_list)
