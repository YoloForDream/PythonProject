from graphviz import Digraph
dot=Digraph(comment='first graphy',filename='firstGraph',format='png',)
dot.graph_attr['bgcolor']='white'
dot.graph_attr['labeljust']='center'
dot.graph_attr['margin']='0.75'
dot.node('a', shape='box', fillcolor='lightblue',style='rounded,filled',label='开始',fontname='Microsoft YaHei')
dot.node('b', shape='parallelogram', fillcolor='lightblue',style='filled',label='请输入数据 n ',fontname='Microsoft YaHei')
dot.edge('a','b',arrowhead='vee')
dot.node('c', shape='rectangle', fillcolor='lightblue',style='filled',label='i=1,s=0',fontname='Microsoft YaHei')
dot.edge('b','c',arrowhead='vee')
dot.node('d', shape='diamond', fillcolor='lightblue',style='filled',label='i<n',fontname='Microsoft YaHei')
dot.edge('c','d',arrowhead='vee')
dot.node('e', shape='rectangle', fillcolor='lightblue',style='filled',label='s+=i',fontname='Microsoft YaHei')
dot.edge('d','e',label='Yes',arrowhead='vee')
dot.node('f', shape='rectangle', fillcolor='lightblue',style='filled',label='i+=1',fontname='Microsoft YaHei')
dot.edge('e','f',arrowhead='vee')
dot.edge('f','d',arrowhead='vee')
dot.node('g', shape='parallelogram', fillcolor='lightblue',style='filled',label='打印 s 的值',fontname='Microsoft YaHei')
dot.edge('d','g',label='No',arrowhead='vee')
dot.node('h', shape='parallelogram', fillcolor='lightblue',style='rounded,filled',label='结束',fontname='Microsoft YaHei')
dot.edge('g','h',arrowhead='vee')
dot.view()