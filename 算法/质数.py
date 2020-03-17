def solution(body1x,body2x,pointx1，pointx2):
    pointx = min(pointx1,pointx2)
    if body1x < pointx and body2x > pointx:
        print('相交')
    elif body2x < pointx:
        print('人在线左侧')
    else:
        print('人在线右侧')

