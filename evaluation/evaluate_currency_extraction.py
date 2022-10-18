#!/usr/bin/env python3
import json
from collections import defaultdict
from time import perf_counter

from price_parser import Price


# Read eval dataset
with open('dataset_eval.json', 'rb') as f:
    dataset_eval = json.load(f)

queries, y_true = list(zip(*[(d['string'], str(d['currency'])) for d in dataset_eval]))

# Extract currency using main function `Price.fromstring` and time it
t0 = perf_counter()
y_pred = [str(Price.fromstring(q).currency) for q in queries]
proc_time_ms = 1000 * (perf_counter() - t0)


# Calculate global accuracy
N = len(queries)
acc_global = len([i for i in range(N) if y_true[i] == y_pred[i]]) / N

# Calculate accuracy per symbol
d_extracted_per_gt = defaultdict(list)
for i in range(N):
    d_extracted_per_gt[y_true[i]].append(y_pred[i])
        
d_acc_per_symbol = {}
for k in [str(None)] + sorted([k for k in d_extracted_per_gt.keys() if k is not None]):
    preds_k = d_extracted_per_gt[k]
    d_acc_per_symbol[k] = len([i for i in range(len(preds_k)) if k == preds_k[i]]) / len(preds_k)

# Print accuracy per symbol in a small table
sep = '-' * 35
print(sep)
print('symbol (target)'.rjust(15) + 'acc'.center(15) + 'support'.ljust(10))
print(sep)
for k in d_acc_per_symbol:
    line = ''
    line += f'{k}'.rjust(15)
    line += f'\u200e{round(d_acc_per_symbol[k], 4)}'.center(15)  # \u200e is LEFT-TO-RIGHT mark, for arabic and others
    line += f'{len(d_extracted_per_gt[k])}'.ljust(10)  # \u200e is LEFT-TO-RIGHT mark, for arabic and others
    print(line)

# Print global acc
print(f'\nGlobal accuracy: {round(acc_global, 4)}\n')

# Print times
print('\nTotal processing time: '.ljust(20) + f'{round(proc_time_ms, 2)} ms')
print('Processing time per sample: '.ljust(20) + f'{round(proc_time_ms / N, 6)} ms')