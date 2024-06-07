"""

Approach: Undirected graph logic does not work for directed graphs,try doing dry run with[[1,2][1,3][2,3].
Hence, we need to make extra data str to get for what nodes dis call has gone hence the nodes dis call is set to true, before making call and set to false after returning.
If for any node the dfs call has gone and the node is also visited then cycle exists.
"""