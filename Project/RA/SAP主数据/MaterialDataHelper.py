import pandas as pd
import stomp
import json
import os
from time import sleep


def read_from_excel():
    path = os.getcwd()
    path = path + '\MaterialData.XLSX'  # 物料数据表
    df = pd.read_excel(path, sheet_name='Sheet2')
    partList = []
    for row in df.itertuples():
        # 定义一个字典用于存储从excel表格存储的数据
        part = {"partNumber": getattr(row, '物料号'), "materialType": getattr(row, '物料类型'),
                "description": getattr(row, '物料描述'), "unitOfMeasure": getattr(row, '基本计量单位'), "gmpName": "",
                "materialGroup": ""}
        if getattr(row, '产成品通用名') != "":
            part["gmpName"] = getattr(row, '产成品通用名')
        else:
            part["gmpName"] = "NA"
        if getattr(row, '物料组') != "":
            part["materialGroup"] = getattr(row, '物料组')
        else:
            part["materialGroup"] = "NA"
        partList.append(part)
    return partList


# 把消息以队列的形式发送给ACTIVEMQ
def send_to_queue(msg):
    try:
        conn = stomp.Connection10([("127.0.0.1", 61613)], auto_content_length=False)  # 127.0.0.1为MQ所在服务器的地址，端口为STOMP端口
        conn.connect()
        conn.send('/queue/part', msg)  # 指定消息格式为queue/队列名称为part
        conn.disconnect()
        return 1
    except Exception as e:
        # logging.error(f"send message with activemq failed, error is:{e}")
        return 0


if __name__ == '__main__':
    partList = []
    partList = read_from_excel()
    for j in range(len(partList)):
        send_to_queue(json.dumps(partList[j]))  # 发送消息到ACTIVEMQ（将Python字典转为JSON数据传输）
        # print('Send Msg--->'+json.dumps(partList[j])+' completed')
        sleep(1)  # 睡眠1秒，预留服务器插写入数据时间
        # print(partList[j])
