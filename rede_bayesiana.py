from pybbn.graph.dag import Bbn
from pybbn.graph.edge import Edge, EdgeType
from pybbn.graph.jointree import EvidenceBuilder
from pybbn.graph.node import BbnNode
from pybbn.graph.variable import Variable
from pybbn.pptc.inferencecontroller import InferenceController
from pre_processamento import gerar_probs_node_avc, gerar_probs_nos_perifericos

def rede_bayesiana(string_entrada):
        probs_nos_perifericos = gerar_probs_nos_perifericos('/home/fsilverio10/mysite/stroke.csv')
        probs_no_avc = gerar_probs_node_avc('/home/fsilverio10/mysite/stroke.csv')

        avc = BbnNode(Variable(0,'avc',['1','0']), [probs_no_avc[0],probs_no_avc[1],probs_no_avc[2],probs_no_avc[3],probs_no_avc[4],probs_no_avc[5],probs_no_avc[6],probs_no_avc[7],probs_no_avc[8],probs_no_avc[9],probs_no_avc[10],probs_no_avc[11],probs_no_avc[12],probs_no_avc[13],probs_no_avc[14],probs_no_avc[15],probs_no_avc[16],probs_no_avc[17],probs_no_avc[18],probs_no_avc[19],probs_no_avc[20],probs_no_avc[21],probs_no_avc[22],probs_no_avc[23],probs_no_avc[24],probs_no_avc[25],probs_no_avc[26],probs_no_avc[27],probs_no_avc[28],probs_no_avc[29],probs_no_avc[30],probs_no_avc[31],probs_no_avc[32],probs_no_avc[33],probs_no_avc[34],probs_no_avc[35],probs_no_avc[36],probs_no_avc[37],probs_no_avc[38],probs_no_avc[39],probs_no_avc[40],probs_no_avc[41],probs_no_avc[42],probs_no_avc[43],probs_no_avc[44],probs_no_avc[45],probs_no_avc[46],probs_no_avc[47],probs_no_avc[48],probs_no_avc[49],probs_no_avc[50],probs_no_avc[51],probs_no_avc[52],probs_no_avc[53],probs_no_avc[54],probs_no_avc[55],probs_no_avc[56],probs_no_avc[57],probs_no_avc[58],probs_no_avc[59],probs_no_avc[60],probs_no_avc[61],probs_no_avc[62],probs_no_avc[63],probs_no_avc[64],probs_no_avc[65],probs_no_avc[66],probs_no_avc[67],probs_no_avc[68],probs_no_avc[69],probs_no_avc[70],probs_no_avc[71],probs_no_avc[72],probs_no_avc[73],probs_no_avc[74],probs_no_avc[75],probs_no_avc[76],probs_no_avc[77],probs_no_avc[78],probs_no_avc[79],probs_no_avc[80],probs_no_avc[81],probs_no_avc[82],probs_no_avc[83],probs_no_avc[84],probs_no_avc[85],probs_no_avc[86],probs_no_avc[87],probs_no_avc[88],probs_no_avc[89],probs_no_avc[90],probs_no_avc[91],probs_no_avc[92],probs_no_avc[93],probs_no_avc[94],probs_no_avc[95],probs_no_avc[96],probs_no_avc[97],probs_no_avc[98],probs_no_avc[99],probs_no_avc[100],probs_no_avc[101],probs_no_avc[102],probs_no_avc[103],probs_no_avc[104],probs_no_avc[105],probs_no_avc[106],probs_no_avc[107],probs_no_avc[108],probs_no_avc[109],probs_no_avc[110],probs_no_avc[111],probs_no_avc[112],probs_no_avc[113],probs_no_avc[114],probs_no_avc[115],probs_no_avc[116],probs_no_avc[117],probs_no_avc[118],probs_no_avc[119],probs_no_avc[120],probs_no_avc[121],probs_no_avc[122],probs_no_avc[123],probs_no_avc[124],probs_no_avc[125],probs_no_avc[126],probs_no_avc[127],probs_no_avc[128],probs_no_avc[129],probs_no_avc[130],probs_no_avc[131],probs_no_avc[132],probs_no_avc[133],probs_no_avc[134],probs_no_avc[135],probs_no_avc[136],probs_no_avc[137],probs_no_avc[138],probs_no_avc[139],probs_no_avc[140],probs_no_avc[141],probs_no_avc[142],probs_no_avc[143],probs_no_avc[144],probs_no_avc[145],probs_no_avc[146],probs_no_avc[147],probs_no_avc[148],probs_no_avc[149],probs_no_avc[150],probs_no_avc[151],probs_no_avc[152],probs_no_avc[153],probs_no_avc[154],probs_no_avc[155],probs_no_avc[156],probs_no_avc[157],probs_no_avc[158],probs_no_avc[159],probs_no_avc[160],probs_no_avc[161],probs_no_avc[162],probs_no_avc[163],probs_no_avc[164],probs_no_avc[165],probs_no_avc[166],probs_no_avc[167],probs_no_avc[168],probs_no_avc[169],probs_no_avc[170],probs_no_avc[171],probs_no_avc[172],probs_no_avc[173],probs_no_avc[174],probs_no_avc[175],probs_no_avc[176],probs_no_avc[177],probs_no_avc[178],probs_no_avc[179],probs_no_avc[180],probs_no_avc[181],probs_no_avc[182],probs_no_avc[183],probs_no_avc[184],probs_no_avc[185],probs_no_avc[186],probs_no_avc[187],probs_no_avc[188],probs_no_avc[189],probs_no_avc[190],probs_no_avc[191],probs_no_avc[192],probs_no_avc[193],probs_no_avc[194],probs_no_avc[195],probs_no_avc[196],probs_no_avc[197],probs_no_avc[198],probs_no_avc[199],probs_no_avc[200],probs_no_avc[201],probs_no_avc[202],probs_no_avc[203],probs_no_avc[204],probs_no_avc[205],probs_no_avc[206],probs_no_avc[207],probs_no_avc[208],probs_no_avc[209],probs_no_avc[210],probs_no_avc[211],probs_no_avc[212],probs_no_avc[213],probs_no_avc[214],probs_no_avc[215],probs_no_avc[216],probs_no_avc[217],probs_no_avc[218],probs_no_avc[219],probs_no_avc[220],probs_no_avc[221],probs_no_avc[222],probs_no_avc[223],probs_no_avc[224],probs_no_avc[225],probs_no_avc[226],probs_no_avc[227],probs_no_avc[228],probs_no_avc[229],probs_no_avc[230],probs_no_avc[231],probs_no_avc[232],probs_no_avc[233],probs_no_avc[234],probs_no_avc[235],probs_no_avc[236],probs_no_avc[237],probs_no_avc[238],probs_no_avc[239],probs_no_avc[240],probs_no_avc[241],probs_no_avc[242],probs_no_avc[243],probs_no_avc[244],probs_no_avc[245],probs_no_avc[246],probs_no_avc[247],probs_no_avc[248],probs_no_avc[249],probs_no_avc[250],probs_no_avc[251],probs_no_avc[252],probs_no_avc[253],probs_no_avc[254],probs_no_avc[255]])
        genero = BbnNode(Variable(1,'genero-masc', ['1','0']), [probs_nos_perifericos[0],probs_nos_perifericos[1]])
        hipertensao = BbnNode(Variable(2,'hipertensao', ['1','0']), [probs_nos_perifericos[2],probs_nos_perifericos[3]])
        doenca_card = BbnNode(Variable(3,'doenca', ['1','0']), [probs_nos_perifericos[4],probs_nos_perifericos[5]])
        tabagismo = BbnNode(Variable(4,'fuma-ja-fumou', ['1','0']), [probs_nos_perifericos[6],probs_nos_perifericos[7]])
        imc = BbnNode(Variable(5,'peso-abaixo-ideal', ['1','0']), [probs_nos_perifericos[8],probs_nos_perifericos[9]])
        glicose = BbnNode(Variable(6,'hipoglicemia-normal', ['1','0']), [probs_nos_perifericos[10],probs_nos_perifericos[11]])
        idade = BbnNode(Variable(7,'jovem-adulto', ['1','0']), [probs_nos_perifericos[12],probs_nos_perifericos[13]])

        bbn = Bbn() \
                .add_node(avc) \
                .add_node(genero) \
                .add_node(hipertensao) \
                .add_node(doenca_card) \
                .add_node(tabagismo) \
                .add_node(imc) \
                .add_node(glicose) \
                .add_node(idade) \
                .add_edge(Edge(genero, avc, EdgeType.DIRECTED)) \
                .add_edge(Edge(doenca_card, avc, EdgeType.DIRECTED)) \
                .add_edge(Edge(tabagismo, avc, EdgeType.DIRECTED)) \
                .add_edge(Edge(imc, avc, EdgeType.DIRECTED)) \
                .add_edge(Edge(glicose, avc, EdgeType.DIRECTED)) \
                .add_edge(Edge(idade, avc, EdgeType.DIRECTED)) \
                .add_edge(Edge(hipertensao, avc, EdgeType.DIRECTED)) \

        join_tree = InferenceController.apply(bbn)

        # quebra da string será realizada aqui
        evidences = list(str(string_entrada))


        ev1 = EvidenceBuilder() \
                .with_node(join_tree.get_bbn_node_by_name('genero-masc')) \
                .with_evidence(evidences[0],1.0) \
                .build()

        ev2 = EvidenceBuilder() \
                .with_node(join_tree.get_bbn_node_by_name('doenca')) \
                .with_evidence(evidences[1],1.0) \
                .build()

        ev3 = EvidenceBuilder() \
                .with_node(join_tree.get_bbn_node_by_name('fuma-ja-fumou')) \
                .with_evidence(evidences[2],1.0) \
                .build()

        ev4 = EvidenceBuilder() \
                .with_node(join_tree.get_bbn_node_by_name('peso-abaixo-ideal')) \
                .with_evidence(evidences[3],1.0) \
                .build()

        ev5 = EvidenceBuilder() \
                .with_node(join_tree.get_bbn_node_by_name('hipoglicemia-normal')) \
                .with_evidence(evidences[4],1.0) \
                .build()

        ev6 = EvidenceBuilder() \
                .with_node(join_tree.get_bbn_node_by_name('jovem-adulto')) \
                .with_evidence(evidences[5],1.0) \
                .build()

        ev7 = EvidenceBuilder() \
                .with_node(join_tree.get_bbn_node_by_name('hipertensao')) \
                .with_evidence(evidences[6],1.0) \
                .build()


        join_tree.set_observation(ev1)
        join_tree.set_observation(ev2)
        join_tree.set_observation(ev3)
        join_tree.set_observation(ev4)
        join_tree.set_observation(ev5)
        join_tree.set_observation(ev6)
        join_tree.set_observation(ev7)

        arq = open('saida.txt','w')

        for node in join_tree.get_bbn_nodes():
                potential = join_tree.get_bbn_potential(node)
                arq.write('\n')
                arq.write(str(potential))




def get_prediction(string_entrada):
        rede_bayesiana(string_entrada)
        arq = open('saida.txt', 'r')
        linhas = arq.readlines()
        tokens = list(linhas)
        tokens2 = list(tokens[15])
        caracteres_escolhidos = []

        for i in range(4,10):
                caracteres_escolhidos.append(tokens2[i])

        porcentagem_string = ''.join(caracteres_escolhidos)
        porc = float(porcentagem_string)

        return porc