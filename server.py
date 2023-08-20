# 필요한 라이브러리를 불러옵니다.
from matplotlib import pyplot as plt
import networkx as nx

# 한글 글꼴 지원을 위한 설정
plt.rc('font', family='Malgun Gothic')

# 그래프 객체를 생성합니다.
G_korean = nx.DiGraph()

# 노드와 엣지를 추가합니다.
G_korean.add_node("사용자")
G_korean.add_node("Dialogflow")
G_korean.add_node("Flask 웹 서버")
G_korean.add_node("MySQL 데이터베이스")

G_korean.add_edge("사용자", "Dialogflow", label="질문")
G_korean.add_edge("Dialogflow", "Flask 웹 서버", label="웹훅 요청")
G_korean.add_edge("Flask 웹 서버", "MySQL 데이터베이스", label="데이터 검색")
G_korean.add_edge("MySQL 데이터베이스", "Flask 웹 서버", label="검색 결과")
G_korean.add_edge("Flask 웹 서버", "Dialogflow", label="응답 생성")
G_korean.add_edge("Dialogflow", "사용자", label="응답")

# 그래프를 그립니다.
pos_korean = nx.spring_layout(G_korean, seed=42)
nx.draw(G_korean, pos_korean, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_color="black", font_weight="bold")
labels_korean = nx.get_edge_attributes(G_korean, 'label')
nx.draw_networkx_edge_labels(G_korean, pos_korean, edge_labels=labels_korean)

# 이미지 파일로 저장합니다.
image_path_korean = "/mnt/data/shipterm_diagram_korean.png"
plt.savefig(image_path_korean)

# 이미지 파일 경로를 반환합니다.
image_path_korean
