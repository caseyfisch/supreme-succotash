"""
andrewId: cjfische
Name:     Casey Fischer

Unit tests for functions.py
"""
import unittest

import paper.database_wrapper as db_wrapper
import paper.functions as funcs
from paper.constants import *

from datetime import datetime
from datetime import timedelta

"""
Constants
"""

USERS = ["alice", "bob", "carlos", "david", "evelyn", "felicia"]
TITLES = ["Oldest Living Yoga Celebrity Tells All", 
          "What is the Color of Beauty?",
          "Paper Cuts",
          "The Thin Gene"
         ]
DESCS = ["'She said they helped elevate her consciousness,' a photographer says of the high heels preferred by Tao Porchon-Lynch.",
         "A multibillion-dollar industry of skin-whitening products dominates the West African beauty market, creating a world of mixed messages for the women who live there.",
         "The Swiss art of Scherenschnitt tells stories in silhouette.",
         "The body of a woman whose mutation keeps her on the brink of starvation may hold the secret to treating obesity."
        ]

TAGS = ["style", "health", "beauty", "opinion"]

ALL_FUNCS = ['add_new_paper', 
             'delete_paper', 
             'get_paper_tags',
             'get_papers_by_keyword', 
             'get_papers_by_tag',
             'get_papers_by_liked', 
             'get_most_active_users',
             'get_most_popular_papers', 
             'get_most_popular_tag_pairs',
             'get_most_popular_tags', 
             'get_number_papers_user', 
             'get_number_tags_user',
             'get_number_liked_user', 
             'get_recommend_papers', 
             'get_timeline',
             'get_timeline_all', 
             'get_likes', 
             'login', 
             'reset_db',
             'signup', 
             'unlike_paper', 
             'like_paper']

RES = {}
VERBOSE = False

class TestFuncMethods(unittest.TestCase):

  def test_signup_valid(self):
    pass
 
  def test_signup_username_too_long(self):
    pass

 
  def test_signup_password_too_long(self):
    pass
 

  def test_signup_username_taken(self):
    pass

 
  def test_login_valid(self):
    pass


  def test_login_user_nonexistent(self):
    pass


  def test_login_password_mismatch(self):
    pass


  def test_add_new_paper_valid(self):
    pass


  def test_add_new_paper_nonalphanumeric_tag(self):
    pass

  
  def test_add_new_paper_tag_too_long(self):
    pass


  def test_add_new_paper_title_too_long(self):
    pass


  def test_add_new_paper_description_too_long(self):
    pass

  
  def test_delete_paper_valid(self):
    pass


  def test_delete_paper_invalid_pid(self):
    pass

  
  def test_get_paper_tags_valid(self):
    pass


  def test_get_paper_tags_invalid_pid(self):
    pass


  def test_like_paper_valid(self):
    pass


  def test_like_paper_author_is_user(self):
    pass


  def test_like_paper_user_already_liked(self):
    pass


  def test_like_paper_invalid_pid(self):
    pass

  
  def test_unlike_paper_valid(self):
    pass

  
  def test_unlike_paper_user_has_not_liked(self):
    pass


  def test_unlike_paper_invalid_pid(self):
    pass


  def test_get_likes_valid(self):
    pass


  def test_get_likes_invalid_pid(self):
    pass


  def test_get_timeline_valid(self):
    pass

 
  def test_get_timeline_smaller_count_than_papers(self):
    pass
  
 
  def test_get_timeline_larger_count_than_papers(self):
    pass


  def test_get_timeline_all_valid(self):
    pass


  def test_get_timeline_all_smaller_count_than_papers(self):
    pass
  

  def test_get_timeline_all_larger_count_than_papers(self):
    pass

 
  def test_get_most_popular_papers_valid(self):
    pass


  def test_get_most_popular_papers_smaller_count_than_papers(self): 
    pass


  def test_get_most_popular_papers_larger_count_than_papers(self):
    pass


  def test_get_most_popular_papers_later_time(self):
    pass


  def test_get_recommend_papers_valid(self):
    pass


  def test_get_recommend_papers_smaller_count_than_papers(self):
    pass


  def test_get_recommend_papers_larger_count_than_papers(self):
    pass


  def test_get_papers_by_tag_valid(self):
    pass

 
  def test_get_papers_by_tag_tag_nonexistent(self):
    pass


  def test_get_papers_by_tag_smaller_count_than_papers(self):
    pass

 
  def test_get_papers_by_tag_larger_count_than_papers(self):
    pass


  def test_get_papers_by_keyword_valid(self):
    pass


  def test_get_papers_by_keyword_keyword_not_found(self):
    pass


  def test_get_papers_by_keyword_smaller_count_than_papers(self):
    pass


  def test_get_papers_by_keyword_larger_count_than_papers(self):
    pass


  def get_papers_by_liked_valid(self):
    pass


  def get_papers_by_liked_smaller_count_than_papers(self):
    pass


  def get_papers_by_liked_larger_count_than_papers(self):
    pass


  def get_most_active_users_valid(self):
    pass
  

  def get_most_active_users_smaller_count_than_users(self):
    pass


  def get_most_active_users_larger_count_than_users(self):
    pass


  def get_most_popular_tags_valid(self):
    pass


  def get_most_popular_tags_smaller_count_than_tags(self):
    pass


  def get_most_popular_tags_larger_count_than_tags(self):
    pass


  def get_most_popular_tag_pairs_valid(self):
    pass


  def get_most_popular_tag_pairs_smaller_count_than_tags(self):
    pass


  def get_most_popular_tag_pairs_larger_count_than_tags(self):
    pass


  def get_number_papers_user_valid(self):
    pass


  def get_number_papers_user_nonexistent(self):
    pass


  def get_number_liked_user_valid(self):
    pass

 
  def get_number_liked_user_nonexistent(self):
    pass


  def get_number_tags_user_valid(self):
    pass

  
  def get_number_tags_user_nonexistent(self):
    pass


suite = unittest.TestLoader().loadTestsFromTestCase(TestFuncMethods)
unittest.TextTestRunner(verbosity = 2).run(suite)
