sci = ['Brain','Star','Mind','Atom','Hyper','Charge','Comet','Galaxy','Mass','Matter','Planet','Fact','Phase','Scale','Lab','Air','Ion']
maths = ['Base','Chaos','Dynamic','Apex','Add','Axes','Axis','Surd','Oval','Plane','Ray','Vertex']
sitech = []
tech = []

for i in range(0,len(sci)):
    for j in range(0,len(maths)):
        print(sci[i]+maths[j])
        print(maths[j]+sci[i])
