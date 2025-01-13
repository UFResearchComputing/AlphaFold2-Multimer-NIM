import requests
import json

url = "http://0:8000/protein-structure/alphafold2/multimer/predict-structure-from-msa"

sequences = ["STARWARSNVIDIAAAAAA"]  # Replace with the actual MSA sequences.

alignments = [{
    'uniref90': ['uniref90', '# STOCKHOLM 1.0\n\n-151285509650596177 STARWARSNVIDIAAAAAA\n#=GC RF             xxxxxxxxxxxxxxxxxxx\n//\n', 'sto'],
    'small_bfd': ['small_bfd', '# STOCKHOLM 1.0\n\n-151285509650596177 STARWARSNVIDIAAAAAA\n#=GC RF             xxxxxxxxxxxxxxxxxxx\n//\n', 'sto']
}]

templates = [
    [{'index': 1, 'name': '5X6U_E Ragulator complex protein LAMTOR3, Ragulator; Ragulator complex, scaffold, roadblock, lysosome; 2.4A {Homo sapiens}', 'aligned_cols': 10, 'sum_probs': 0.0, 'query': 'RSNVIDIAAA', 'hit_sequence': 'ASNIIDVSAA', 'indices_query': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'indices_hit': [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]}, {'index': 2, 'name': '5X6V_E Ragulator complex protein LAMTOR3, Ragulator; Ragulator Rag GTPase complex, scaffold; 2.02A {Homo sapiens}', 'aligned_cols': 10, 'sum_probs': 7.9, 'query': 'RSNVIDIAAA', 'hit_sequence': 'ASNIIDVSAA', 'indices_query': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'indices_hit': [23, 24, 25, 26, 27, 28, 29, 30, 31, 32]}, {'index': 3, 'name': '6EHP_E Ragulator complex protein LAMTOR3, Ragulator; Scaffolding complex, Rag-GTPase, mTOR, Ragulator; 2.3A {Homo sapiens}', 'aligned_cols': 10, 'sum_probs': 0.0, 'query': 'RSNVIDIAAA', 'hit_sequence': 'ASNIIDVSAA', 'indices_query': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'indices_hit': [45, 46, 47, 48, 49, 50, 51, 52, 53, 54]}, {'index': 4, 'name': '6EHR_E Ragulator complex protein LAMTOR3, Ragulator; Scaffolding complex, Rag-GTPases, mTOR, Ragulator; 2.898A {Homo sapiens}', 'aligned_cols': 10, 'sum_probs': 7.8, 'query': 'RSNVIDIAAA', 'hit_sequence': 'ASNIIDVSAA', 'indices_query': [6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'indices_hit': [45, 46, 47, 48, 49, 50, 51, 52, 53, 54]}, {'index': 5, 'name': '6CTD_B Large-conductance mechanosensitive channel; Channel Mechanosensitive Mycobacterium tuberculosis, MEMBRANE; 5.8A {Mycobacterium tuberculosis (strain ATCC 25177 / H37Ra)}', 'aligned_cols': 11, 'sum_probs': 8.7, 'query': 'ARSNVIDIAAA', 'hit_sequence': 'ARGNIVDLAVA', 'indices_query': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'indices_hit': [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]}, {'index': 6, 'name': '3HZQ_A Large-conductance mechanosensitive channel; intermediate state Mechanosensitive channel osmoregulation; 3.82A {Staphylococcus aureus subsp. aureus MW2}', 'aligned_cols': 11, 'sum_probs': 8.6, 'query': 'ARSNVIDIAAA', 'hit_sequence': 'LKGNVLDLAIA', 'indices_query': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'indices_hit': [29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]}, {'index': 7, 'name': '6B9X_A Ragulator complex protein LAMTOR1, Ragulator; Ragulator, Lamtor, SIGNALING PROTEIN; 1.42A {Homo sapiens}', 'aligned_cols': 12, 'sum_probs': 0.0, 'query': 'WARSNVIDIAAA', 'hit_sequence': 'KTASNIIDVSAA', 'indices_query': [4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'indices_hit': [59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70]}, {'index': 8, 'name': '4V7H_BM Ribosome; eukaryotic ribosome, 80S, RACK1 protein; HET: OMC, PSU, 5MU, 1MA, OMG, 5MC, YYG, 7MG, 2MG, H2U, M2G; 8.9A {Thermomyces lanuginosus}', 'aligned_cols': 15, 'sum_probs': 9.1, 'query': 'RWARSNVIDIAAAAA', 'hit_sequence': 'GWKAAAAAAAAAAAA', 'indices_query': [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 'indices_hit': [139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153]}, {'index': 9, 'name': '6QKP_A Nucleoid-associated protein Lsr2; Tuberculosis, DNA organisation, Transcriptional regulator; NMR {Mycobacterium tuberculosis (strain ATCC 25618 / H37Rv)}', 'aligned_cols': 12, 'sum_probs': 9.2, 'query': 'RWARSNVIDIAA', 'hit_sequence': 'EWARRNGHNVST', 'indices_query': [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 'indices_hit': [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]}, {'index': 10, 'name': "1QGN_F CYSTATHIONINE GAMMA-SYNTHASE; METHIONINE BIOSYNTHESIS, PYRIDOXAL 5'-PHOSPHATE, GAMMA-FAMILY; HET: PLP; 2.9A {Nicotiana tabacum} SCOP: c.67.1.3", 'aligned_cols': 10, 'sum_probs': 0.0, 'query': 'NVIDIAAAAA', 'hit_sequence': 'KAVDAAAAAA', 'indices_query': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17], 'indices_hit': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}, {'index': 11, 'name': '2OAR_E Large-conductance mechanosensitive channel; stretch activated ion channel mechanosensitive; 3.5A {Mycobacterium tuberculosis H37Ra} SCOP: f.16.1.1', 'aligned_cols': 11, 'sum_probs': 8.9, 'query': 'ARSNVIDIAAA', 'hit_sequence': 'ARGNIVDLAVA', 'indices_query': [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 'indices_hit': [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]}, {'index': 12, 'name': '5XKX_A Flavin-containing monooxygenase; Dimethylsulfoniopropionate (DMSP) lyase, LYASE; 1.5A {Acinetobacter bereziniae NIPH 3}', 'aligned_cols': 10, 'sum_probs': 8.0, 'query': 'ARWARSNVID', 'hit_sequence': 'TVWARTTAQD', 'indices_query': [2, 3, 4, 5, 6, 7, 8, 9, 10, 11], 'indices_hit': [356, 357, 358, 359, 360, 361, 362, 363, 364, 365]}]
]

headers = {
    "content-type": "application/json"
}

data = {
    "sequences": sequences,
    "alignments": alignments,
    "templates": templates
}

response = requests.post(url, headers=headers, data=json.dumps(data))

# Check if the request was successful
if response.ok:
    print("Request succeeded:", response.json())
else:
    print("Request failed:", response.status_code, response.text)
