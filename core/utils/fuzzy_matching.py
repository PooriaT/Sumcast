from thefuzz import fuzz
from thefuzz import process


def fuzzy_match(source_text, input_text):
    return fuzz.ratio(source_text, input_text)


def fuzzy_match_with_threshold(source_text, input_text, threshold):
    return fuzz.ratio(source_text, input_text) >= threshold


def fuzzy_match_with_threshold_and_limit(source_text, input_text, threshold):
    return process.extractOne(source_text, input_text, scorer=fuzz.ratio, score_cutoff=threshold)
