# Bitcoin Analysis

This repository contains scripts that have been used for analysis of the bitcoin blockchain.

The results of these analysis have been presented in [The Facebook of financial transactions - User Tracking on the Bitcoin Blockchain](https://media.ccc.de/v/FWTYS3) on the [MRMCD 17](https://2017.mrmcd.net/index.en.html).

It might be updated as analysis continues. As this is a hobby project, don't expect it to happen too frequently or at all.

The repo is divided in three parts that should be quite self-explanatory:

  * preparation
  * analysis
  * visualisation


# Dependencies

This project is carried out using Antoine Le Calvez' [Blockchain Parser](https://github.com/alecalve/python-bitcoin-blockchain-parser) library.


# Drawbacks

Most of these scripts are written with a lot of available memory in mind as they keep all the blockchain-data in memory during analysis, so they will likely run out of memory when run on your machine. In that case, rebasing the codes onto something like mongodb can likely solve the issue if you want to run the codes yourself.
