# Homework 11: Wordle Assistant

## Overview
This script acts as a Wordle puzzle solver. It parses a text file of words, filters out invalid options (words with duplicates, lengths other than 5, or ending in 's'), and provides functions to narrow down possibilities based on known letter inclusions, exclusions, and exact positional matches.

## Concepts Covered
* File I/O (`open`, `.readlines()`)
* Set operations (intersections, subsets)
* Dictionaries (mapping letters to positions)
* List comprehensions