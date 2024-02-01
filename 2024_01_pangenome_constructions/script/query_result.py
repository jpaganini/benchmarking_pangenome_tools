import igraph as ig
from tqdm import tqdm
import networkx as nx
import csv

#ggcaller
# Reading ggcaler GML file
ggcaller_file_path = '../../2024_01_pangenome_constructions/results/ggcaller_result/final_graph.gml'
ggcaller_graph = ig.load(ggcaller_file_path, format='gml')

# Query the number of nodes and edges
ggcaller_num_nodes = ggcaller_graph.vcount()
ggcaller_num_edges = ggcaller_graph.ecount()
ggcaller_num_subgraphs = ggcaller_graph.decompose()
print("ggcaller finished")

#Panaroo
# Reading panaroo GML file
panaroo_file_path = '../../2024_01_pangenome_constructions/results/panaroo_bakta_result/final_graph.gml'
panaroo_graph = ig.load(panaroo_file_path, format='gml')

# Query the number of nodes and edges
panaroo_num_nodes = panaroo_graph.vcount()
panaroo_num_edges = panaroo_graph.ecount()
panaroo_num_subgraphs = panaroo_graph.decompose()
print("Panaroo finished")

#Pangraph
def pangraph_to_igraph(gfa_file):
    # Creating a igraph
    pangraph_graph = ig.Graph()

    # Used to keep track of edges that have been added to avoid duplicate additions
    added_edges = set()

    # Get total number of lines in this file
    total_lines = sum(1 for line in open(gfa_file, 'r'))

    with open(gfa_file, 'r') as file:
        # Adding a progress bar with tqdm
        for line in tqdm(file, desc="Processing Pangraph", unit=" lines", total=total_lines):
            if line.startswith('S'):  # Node 
                _, node_id, _, _, _, = line.strip().split('\t')
                pangraph_graph.add_vertex(name=node_id)
            elif line.startswith('L'):  # Edge
                _, source, source_orient, target, target_orient, _, _, = line.strip().split('\t')

                # Remove same but opposite edges 
                forward_edge = (source, target, source_orient, target_orient)
                reverse_edge = (target, source, '-' if target_orient == '+' else '+', '-' if source_orient == '+' else '+')

                if forward_edge not in added_edges and reverse_edge not in added_edges:
                    pangraph_graph.add_edge(source, target, source_orient=source_orient, target_orient=target_orient)
                    added_edges.add(forward_edge)


    return pangraph_graph

# PPanGGOLiN
def PPanGGOLiN_to_igraph(input_file):
    # Creating an igraph
    graph = ig.Graph()

    # Used to keep track of edges that have been added to avoid duplicate additions
    added_edges = set()

    # Used to keep track of nodes that have been added to avoid duplicate additions
    added_nodes = set()
    total_lines = sum(1 for line in open(input_file, 'r'))

    with open(input_file, 'r') as file:
        for line in tqdm(file, desc="Processing PPanGGOLiN", unit=" lines", total=total_lines):
            # Process nodes
            if '<node' in line and 'id=' in line:
                node_id = line.split('id="')[1].split('"')[0]
                node_label = line.split('label="')[1].split('"')[0]
                graph.add_vertex(name=node_id, label=node_label)
                added_nodes.add(node_id)

            # Process edges
            elif '<edge' in line and 'id=' in line:
                edge_id = line.split('id="')[1].split('"')[0]
                source = line.split('source="')[1].split('"')[0]
                target = line.split('target="')[1].split('"')[0]

                # Ensure source and target nodes exist before adding the edge
                if source in added_nodes and target in added_nodes:
                    edge_name = f"{edge_id}"  # You can customize the edge name as needed
                    if edge_name not in added_edges:
                        graph.add_edge(source, target, name=edge_name)
                        added_edges.add(edge_name)

    return graph


#bifrost
def bifrost_to_igraph(gfa_file):
    # Creating a igraph
    graph = ig.Graph()

    # Used to keep track of edges that have been added to avoid duplicate additions
    added_edges = set()

    # Get total number of lines in this file
    total_lines = sum(1 for line in open(gfa_file, 'r'))

    with open(gfa_file, 'r') as file:
        # Adding a progress bar with tqdm
        for line in tqdm(file, desc="Processing bifrost", unit=" lines", total=total_lines):
            if line.startswith('S'):  # Node 
                _, node_id, sequence = line.strip().split('\t')
                graph.add_vertex(name=node_id, sequence=sequence)

            elif line.startswith('L'):  # Edge
                _, source, source_orient, target, target_orient, length = line.strip().split('\t')

                # Remove same but opposite edges 
                forward_edge = (source, target, source_orient, target_orient)
                reverse_edge = (target, source, '-' if target_orient == '+' else '+', '-' if source_orient == '+' else '+')

                if forward_edge not in added_edges and reverse_edge not in added_edges:
                    graph.add_edge(source, target, source_orient=source_orient, target_orient=target_orient)
                    added_edges.add(forward_edge)


    return graph

#cuttlefish
def cuttlefish_to_igraph(gfa_file):
    # Creating an igraph
    graph = ig.Graph()

    # Used to keep track of edges that have been added to avoid duplicate additions
    added_edges = set()

    # Get total number of lines in this file
    total_lines = sum(1 for line in open(gfa_file, 'r'))

    with open(gfa_file, 'r') as file:
        # Process lines starting with 'S'
        for line in tqdm(file, desc="Processing cuttlefish nodes", unit=" lines", total=total_lines):
            if line.startswith('S'):  # Node 
                _, node_id, sequence, _ = line.strip().split('\t')
                graph.add_vertex(name=node_id, sequence=sequence)

        # Reset file pointer to the beginning of the file for processing 'L' lines
        file.seek(0)

        # Process lines starting with 'L'
        for line in tqdm(file, desc="Processing cuttlefish edges", unit=" lines", total=total_lines):
            if line.startswith('L'):  # Edge
                _, source, source_orient, target, target_orient, length = line.strip().split('\t')

                # Remove same but opposite edges 
                forward_edge = (source, target, source_orient, target_orient)
                reverse_edge = (target, source, '-' if target_orient == '+' else '+', '-' if source_orient == '+' else '+')

                if forward_edge not in added_edges and reverse_edge not in added_edges:
                    graph.add_edge(source, target, source_orient=source_orient, target_orient=target_orient)
                    added_edges.add(forward_edge)

    return graph

#ggcaller
# Write the result to the TSV file
ggcaller_output_file_path = '../../2024_01_pangenome_constructions/results/query_result/ggcaller_results.tsv'
with open(ggcaller_output_file_path, 'w', newline='') as output_file:
    writer = csv.writer(output_file, delimiter='\t')

    # Write the number of nodes and edges
    writer.writerow([f"Number of nodes: {ggcaller_num_nodes}"])
    writer.writerow([f"Number of edges: {ggcaller_num_edges}"])
    writer.writerow([f"Number of subgraphs: {len(ggcaller_num_subgraphs)}"])
    # Write in the title line
    writer.writerow([f"Node degrees:"])

    # Write the degree of each node
    for node in range(ggcaller_num_nodes):
        degree = ggcaller_graph.degree(node)
        writer.writerow([node, degree])

#panaroo
# rite the result to the TSV file
panaroo_output_file_path = '../../2024_01_pangenome_constructions/results/query_result/panaroo_results.tsv'
with open(panaroo_output_file_path, 'w', newline='') as output_file:
    writer = csv.writer(output_file, delimiter='\t')

    # Write the number of nodes and edges
    writer.writerow([f"Number of nodes: {panaroo_num_nodes}"])
    writer.writerow([f"Number of edges: {panaroo_num_edges}"])
    writer.writerow([f"Number of subgraphs: {len(panaroo_num_subgraphs)}"])
    # Write in the title line
    writer.writerow([f"Node degrees:"])

    for node in range(panaroo_num_nodes):
        degree = panaroo_graph.degree(node)
        writer.writerow([node, degree])


#pangraph
pangraph_file_path = '../../2024_01_pangenome_constructions/results/pangraph_result/pangraph.gfa'
pangraph_output_igraph = pangraph_to_igraph(pangraph_file_path)

# Write result ro tsv file
pangraph_output_file_path = '../../2024_01_pangenome_constructions/results/query_result/pangraph_results.tsv'

# Write no. of node to outputfile
with open(pangraph_output_file_path, 'w') as output_file:
    output_file.write(f"Number of nodes: {pangraph_output_igraph.vcount()}\n")

# Write no. of edge to outputfile
with open(pangraph_output_file_path, 'a') as output_file:
    output_file.write(f"Number of edges: {pangraph_output_igraph.ecount()}\n")

with open(pangraph_output_file_path, 'a') as output_file:
    pangraph_subgraphs = pangraph_output_igraph.decompose()
    output_file.write(f"Number of subgraphs: {len(pangraph_subgraphs)}\n")

# Write degree of node to outputfile
node_degrees = list(zip(pangraph_output_igraph.vs["name"], pangraph_output_igraph.degree()))  
with open(pangraph_output_file_path, 'a') as output_file:
    output_file.write(f"Node degrees: {node_degrees}\n")

#PPanGGOLiN
PPanGGOLiN_file_path = '../../2024_01_pangenome_constructions/results/ppanggolin_result/pangenomeGraph.gexf' 
PPanGGOLiN_output_igraph = PPanGGOLiN_to_igraph(PPanGGOLiN_file_path)

# Write the results to a TSV file
PPanGGOLiN_output_file_path = '../../2024_01_pangenome_constructions/results/query_result/PPanGGOLiN_results.tsv'

# Write the number of nodes to the output file
with open(PPanGGOLiN_output_file_path, 'w') as output_file:
    output_file.write(f"Number of nodes: {PPanGGOLiN_output_igraph.vcount()}\n")

# Write the number of edges to the output file
with open(PPanGGOLiN_output_file_path, 'a') as output_file:
    output_file.write(f"Number of edges: {PPanGGOLiN_output_igraph.ecount()}\n")

with open(PPanGGOLiN_output_file_path, 'a') as output_file:
    PPanGGOLiN_subgraphs = PPanGGOLiN_output_igraph.decompose()
    output_file.write(f"Number of subgraphs: {len(PPanGGOLiN_subgraphs)}\n")

# Write node degree to output file
node_degrees = list(zip(PPanGGOLiN_output_igraph.vs["name"], PPanGGOLiN_output_igraph.degree(mode="in"))) 
with open(PPanGGOLiN_output_file_path, 'a') as output_file:
    output_file.write(f"Node in-degrees: {node_degrees}\n")

#bifrost
bifrost_file_path = '../../2024_01_pangenome_constructions/results/bifrost_result/bifrost_graph.gfa'
bifrost_output_igraph = bifrost_to_igraph(bifrost_file_path)

# Write result ro tsv file
bifrost_output_file_path = '../../2024_01_pangenome_constructions/results/query_result/bifrost_results.tsv'

# Write no. of node to outputfile
with open(bifrost_output_file_path, 'w') as output_file:
    output_file.write(f"Number of nodes: {bifrost_output_igraph.vcount()}\n")

# Write no. of edge to outputfile
with open(bifrost_output_file_path, 'a') as output_file:
    output_file.write(f"Number of edges: {bifrost_output_igraph.ecount()}\n")

with open(bifrost_output_file_path, 'a') as output_file:
    bifrost_subgraphs = bifrost_output_igraph.decompose()
    output_file.write(f"Number of subgraphs: {len(bifrost_subgraphs)}\n")

# Write degree of node to outputfile
node_degrees = list(zip(bifrost_output_igraph.vs["name"], bifrost_output_igraph.degree())) 
with open(bifrost_output_file_path, 'a') as output_file:
    output_file.write(f"Node degrees: {node_degrees}\n")


#cuttlefish
cuttlefish_file_path = '../../2024_01_pangenome_constructions/results/cuttlefish_result/cuttlefish_gfa1.gfa1'
cuttlefish_output_igraph = cuttlefish_to_igraph(cuttlefish_file_path)

# Write result ro tsv file
cuttlefish_output_file_path = '../../2024_01_pangenome_constructions/results/query_result/cuttlefish_gfa1.tsv'

# Write no. of node to outputfile
with open(cuttlefish_output_file_path, 'w') as output_file:
    output_file.write(f"Number of nodes: {cuttlefish_output_igraph.vcount()}\n")

# Write no. of edge to outputfile
with open(cuttlefish_output_file_path, 'a') as output_file:
    output_file.write(f"Number of edges: {cuttlefish_output_igraph.ecount()}\n")

with open(cuttlefish_output_file_path, 'a') as output_file:
    cuttlefish_subgraphs = cuttlefish_output_igraph.decompose()
    output_file.write(f"Number of subgraphs: {len(cuttlefish_subgraphs)}\n")

# Write degree of node to outputfile
node_degrees = list(zip(cuttlefish_output_igraph.vs["name"], cuttlefish_output_igraph.degree())) 
with open(cuttlefish_output_file_path, 'a') as output_file:
    output_file.write(f"Node degrees: {node_degrees}\n")




