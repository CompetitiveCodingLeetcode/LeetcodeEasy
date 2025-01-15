"""
### Time

You will have 55 minutes to complete this question. However, there may be follow-up questions after you complete this task. Use your time wisely.

### Introduction

*Reconciliation* is a term Addepar uses for a set of correctness and consistency measures applied to the data we receive and use in financial calculations.

One of the most common reconciliation checks is called *unit reconciliation*, which answers the question

*Does the transaction history add up to the number of shares the bank says I have?*

For example, if the bank said I had 100 shares of Apple at the end of yesterday, and I bought 20 shares of Apple today, then we expect the bank to report 120 shares at the end of today. This surprisingly isn't always the case! The bank may send incomplete data, we may be parsing it incorrectly, or there may be events like corporate actions or trade settlement lag that cause an inconsistency.

Unit reconciliation is very important because numbers that don't add up shouldn't be trusted for any metrics.

### The Ask

Write a function that takes three lists of strings as input:

* D0-POS
    - describes the positions in the account at the end of day 0. Each record is a space-separated pair of symbol and shares. For example, "AAPL 10" means 10 shares of AAPL were held at the end of day 0, and "Cash 122.16" means we had $122.16 in the account at the end of day 0.

* D1-TRN
    - describes the transactions that occurred in the account on day 1.  Each record is a space-separated collection. The first column is the transaction code, remaining columns depend on the given transaction code.

* D1-POS
    - describes the positions in the account at the end of day 1, and has the same format as `D0-POS`.

And outputs a list of positions with unit reconciliation errors:
* Each record is a space-separated pair of symbol and difference between the actual quantities and the expected ones
* Only positions with unit reconciliation problems should appear in the list
* The list should be empty if no reconciliation issues are found
* For example: "GOOG 10" indicates we ended up the day with 10 extra shares of GOOG that were not explained by the intra-day transactions, while "Cash -10" shows that we ended the day with 10 fewer units of cash than expected

To start us off, let's support two basic transaction types and a single cash currency (assume USD):

* Buy [BY]
    - Besides the first two generic fields, two additional ones: units, and total value
    - For example, "AAPL BY 10 6123.21" means 10 shares of AAPL were bought for a total cost of $6123.21
Sell [SL]
* Same as `BY` case, but sells shares for dollars

### Sample Input
    ["AAPL 100", "GOOG 200", "Cash 10"] # D0-POS

    ["AAPL SL 50 30000", "GOOG BY 10 10000"] # D1-TRN

    ["AAPL 50", "GOOG 220", "Cash 20000"] # D1-POS

### Sample Output
    ["GOOG 10", "Cash -10"]
"""


def reconcile(pos0, txn1, pos1):
    """
    Flags unit reconciliation problems.

    :param pos0: list of positions end of day 0
    :param txn1: list of transactions day 1
    :param pos1: list of positions end of day 1
    :return: list of reconciliation issues


    initial = {
    "AAPL": [50]
    GOOG: [210]
    Cash: [2010]}


    """
    initial_share_info = {}
    for share_info in pos0:
        share_name_qty = share_info.split(" ")
        if share_name_qty[0] not in initial_share_info.keys():
            initial_share_info[share_name_qty[0]] = int(share_name_qty[1])

    if "Cash" not in initial_share_info.keys():
        initial_share_info["Cash"] = 0

    for transaction in txn1:
        txn_details = transaction.split(" ")
        if txn_details[0] in initial_share_info.keys():
            if txn_details[1] == "SL":
                initial_share_info[txn_details[0]] -= int(txn_details[2])
                initial_share_info["Cash"] += int(txn_details[3])
            elif txn_details[1] == "BY":
                initial_share_info[txn_details[0]] += int(txn_details[2])
                initial_share_info["Cash"] -= int(txn_details[3])
        else:
            if txn_details[1] == "SL":
                initial_share_info[txn_details[0]] = -1 * int(txn_details[2])
                initial_share_info["Cash"] += int(txn_details[3])
            elif txn_details[1] == "BY":
                initial_share_info[txn_details[0]] = int(txn_details[2])
                initial_share_info["Cash"] -= int(txn_details[3])

    rec_details = {}
    for rec_info in pos1:
        rec = rec_info.split(" ")
        if rec[0] not in rec_details.keys():
            rec_details[rec[0]] = int(rec[1])

    diff = []
    for k, v in rec_details.items():
        if k not in initial_share_info.keys():
            diff.append(f"{k} {v}")
        elif initial_share_info[k] != v:
            discrepancy = v - initial_share_info[k]
            diff.append(f"{k} {discrepancy}")

    initial_shares = initial_share_info.keys()
    rec_details_shares = rec_details.keys()
    shares_missed = initial_shares - rec_details_shares

    for share in shares_missed:
        val = -1 * initial_share_info[share]
        diff.append(f"{share} {val}")

    print(diff)
    return diff


if __name__ == "__main__":
    pos0 = ["AAPL 100", "GOOG 200", "Cash 10"]  # D0-POS
    txn1 = ["AAPL SL 25 15000", "GOOG BY 20 10000", "AAPL SL 25 10000", "META SL 5 5000"]  # D1-TRN
    pos1 = ["AAPL 50", "GOOG 220", "Cash 20000"]  # D1-POS
    reconcile(pos0, txn1, pos1)