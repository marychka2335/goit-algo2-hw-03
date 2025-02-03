import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

# Побудова графа
G = nx.DiGraph()

# Додавання вершин і ребер
edges = [
    ('Terminal 1', 'Warehouse 1', 25),
    ('Terminal 1', 'Warehouse 2', 20),
    ('Terminal 1', 'Warehouse 3', 15),
    ('Terminal 2', 'Warehouse 3', 15),
    ('Terminal 2', 'Warehouse 4', 30),
    ('Terminal 2', 'Warehouse 2', 10),
    ('Warehouse 1', 'Store 1', 15),
    ('Warehouse 1', 'Store 2', 10),
    ('Warehouse 1', 'Store 3', 20),
    ('Warehouse 2', 'Store 4', 15),
    ('Warehouse 2', 'Store 5', 10),
    ('Warehouse 2', 'Store 6', 25),
    ('Warehouse 3', 'Store 7', 20),
    ('Warehouse 3', 'Store 8', 15),
    ('Warehouse 3', 'Store 9', 10),
    ('Warehouse 4', 'Store 10', 20),
    ('Warehouse 4', 'Store 11', 10),
    ('Warehouse 4', 'Store 12', 15),
    ('Warehouse 4', 'Store 13', 5),
    ('Warehouse 4', 'Store 14', 10)
]

for u, v, capacity in edges:
    G.add_edge(u, v, capacity=capacity)

# Застосування алгоритму Едмондса-Карпа
flow_value, flow_dict = nx.maximum_flow(G, 'Terminal 1', 'Store 14')

# Аналіз результатів
print(f"Максимальний потік: {flow_value}")
print("Потік через ребра:")
for u in flow_dict:
    for v in flow_dict[u]:
        if flow_dict[u][v] > 0:
            print(f"{u} -> {v}: {flow_dict[u][v]}")

# Візуалізація графа
pos = nx.spring_layout(G)
edge_labels = nx.get_edge_attributes(G, 'capacity')
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()

# Підготовка таблиці результатів
result_table = []
for terminal in ['Terminal 1', 'Terminal 2']:
    for store in ['Store 1', 'Store 2', 'Store 3', 'Store 4', 'Store 5', 'Store 6',
                  'Store 7', 'Store 8', 'Store 9', 'Store 10', 'Store 11', 'Store 12',
                  'Store 13', 'Store 14']:
        flow = sum(flow_dict.get(terminal, {}).get(warehouse, {}).get(store, 0) for warehouse in G.neighbors(terminal))
        result_table.append({'Термінал': terminal, 'Магазин': store, 'Фактичний Потік (одиниць)': flow})

# Вивід таблиці результатів
df = pd.DataFrame(result_table)
print(df)

# Відповіді на питання аналізу
def analyze_results():
    # Питання 1: Які термінали забезпечують найбільший потік товарів до магазинів?
    terminal_flow = df.groupby('Термінал')['Фактичний Потік (одиниць)'].sum()
    print("\nТермінали з найбільшим потоком товарів до магазинів:")
    print(terminal_flow)

    # Питання 2: Які маршрути мають найменшу пропускну здатність і як це впливає на загальний потік?
    min_capacity_routes = [edge for edge, capacity in nx.get_edge_attributes(G, 'capacity').items() if capacity == min(edge_labels.values())]
    print("\nМаршрути з найменшою пропускною здатністю:")
    print(min_capacity_routes)

    # Питання 3: Які магазини отримали найменше товарів і чи можна збільшити їх постачання, збільшивши пропускну здатність певних маршрутів?
    store_flow = df.groupby('Магазин')['Фактичний Потік (одиниць)'].sum()
    min_flow_stores = store_flow[store_flow == store_flow.min()]
    print("\nМагазини, що отримали найменше товарів:")
    print(min_flow_stores)

    # Питання 4: Чи є вузькі місця, які можна усунути для покращення ефективності логістичної мережі?
    # Вузькі місця — це маршрути з найменшою пропускною здатністю
    print("\nВузькі місця, які можна усунути:")
    print(min_capacity_routes)

analyze_results()
