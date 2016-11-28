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
DESCS = ["Description one", "Description two", "Description three", "Description four"]
TEXTS = ["'She said they helped elevate her consciousness,' a photographer says of the high heels preferred by Tao Porchon-Lynch.",
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


def db_wrapper_debug(func, argdict, verbose = True):
  res = db_wrapper.call_db(func, argdict)
  return res


class TestFuncMethods(unittest.TestCase):

  def setUp(self):
    # reset database and add in some dummy values to work with later
    try:
      status, res = db_wrapper_debug(funcs.reset_db, {})

    except Exception as e:
      print e
      raise 

    try:
      for user in USERS:
        status, res = db_wrapper_debug(funcs.signup, {'uname': user, 'pwd': user})
        if (status != SUCCESS):
          status_error(funcs.signup)

      status, res = db_wrapper_debug(funcs.add_new_paper, {'uname': USERS[0], 
          'title': TITLES[0], 'desc': DESCS[0], 'text': TEXTS[0], 'tags': [TAGS[0], TAGS[1]]})

      status, res = db_wrapper_debug(funcs.add_new_paper, {'uname': USERS[0], 
          'title': TITLES[1], 'desc': DESCS[1], 'text': TEXTS[1], 'tags': [TAGS[0], TAGS[3]]})

      status, res = db_wrapper_debug(funcs.add_new_paper, {'uname': USERS[1], 
          'title': TITLES[2], 'desc': DESCS[2], 'text': TEXTS[2], 'tags': [TAGS[0], TAGS[1]]})

      status, res = db_wrapper_debug(funcs.add_new_paper, {'uname': USERS[2], 
          'title': TITLES[3], 'desc': DESCS[3], 'text': TEXTS[3], 'tags': [TAGS[1], TAGS[2]]})

    except Exception as e:
      pass
      raise 
 

  def test_signup_valid(self):
    try:
      status, res = db_wrapper_debug(funcs.signup, {'uname': 'george', 'pwd': 'george'})

      self.assertEqual(status, SUCCESS)
      self.assertIsNone(res)
    except Exception as e:
      print e
      raise 

 
  def test_signup_username_too_long(self):
    try:
      long_user = "asdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdfasdf"
      status, res = db_wrapper_debug(funcs.signup, {'uname': long_user, 'pwd': 'short'})
      
      self.assertEqual(status, 2)
      self.assertEqual(res, None)
    except Exception as e:
      print e
      raise 

 
  def test_signup_password_too_long(self):
    try:
      long_pass = "asdfasdfasdfasdfasdfasdfasdfasdfasdfasdf"
      status, res = db_wrapper_debug(funcs.signup, {'uname': 'casey', 'pwd': long_pass})
      
      self.assertEqual(status, 2)
      self.assertIsNone(res)
    except Exception as e:
      print e
      raise 


  def test_signup_username_taken(self):
    try:
      existing_user = 'alice'
      status, res = db_wrapper_debug(funcs.signup, {'uname': existing_user, 'pwd': 'diff'})
   
      self.assertEqual(status, 1)
      self.assertIsNone(res) 
    except Exception as e:
      print e
      raise 

 
  def test_login_valid(self):
    try:
      user = USERS[0]
      status, res = db_wrapper_debug(funcs.login, {'uname': user, 'pwd': user})
     
      self.assertEqual(status, SUCCESS)
      self.assertIsNone(res)      
    except Exception as e:
      print e
      raise 


  def test_login_user_nonexistent(self):
    try:
      non_user = 'casey'
      status, res = db_wrapper_debug(funcs.login, {'uname': non_user, 'pwd': non_user})
   
      self.assertEqual(status, 1)
      self.assertIsNone(res)
    except Exception as e:
      print e
      raise 


  def test_login_password_mismatch(self):
    try:
      user = USERS[0]
      pwd  = USERS[1]
      status, res = db_wrapper_debug(funcs.login, {'uname': user, 'pwd': pwd})

      self.assertEqual(status, 2)
      self.assertIsNone(res)
    except Exception as e:
      print e
      raise 


  def test_add_new_paper_valid(self):
    try:
      user = USERS[2]
      title = "Test paper title"
      desc = "Test paper description"
      text = "Test paper text foo bar foo"
      tags = ["tag1", "tag2", "tag3", TAGS[0]]

      status, res = db_wrapper_debug(funcs.add_new_paper, {'uname': user, 'title': title,
          'desc': desc, 'text': text, 'tags': tags})

      self.assertEqual(status, SUCCESS)
      self.assertIsNotNone(res)
    except Exception as e:
      print e
      raise 


  def test_add_new_paper_nonalphanumeric_tag(self):
    try:
      user = USERS[2]
      title = "Test paper title"
      desc = "Test paper description"
      text = "Test paper text foo bar foo"
      tags = ["what???"]

      status, res = db_wrapper_debug(funcs.add_new_paper, {'uname': user, 'title': title,
          'desc': desc, 'text': text, 'tags': tags})

      self.assertEqual(status, 1)
      self.assertIsNone(res)
    except Exception as e:
      print e
      raise 

  
  def test_add_new_paper_title_too_long(self):
    try:
      user = USERS[2]
      title = "Long title is long long title is long long title is long long title is long long title is long"
      desc = "Test paper description"
      text = "Test paper text foo bar foo"
      tags = ["turkey"]

      status, res = db_wrapper_debug(funcs.add_new_paper, {'uname': user, 'title': title,
          'desc': desc, 'text': text, 'tags': tags})

      self.assertEqual(status, 1)
      self.assertIsNone(res)
    except Exception as e:
      print e
      raise 
   

  def test_add_new_paper_tag_too_long(self):
    try:
      user = USERS[2]
      title = "Test paper title"
      desc = "Test paper description"
      text = "Test paper text foo bar foo"
      tags = ["tagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtagtag"]

      status, res = db_wrapper_debug(funcs.add_new_paper, {'uname': user, 'title': title,
          'desc': desc, 'text': text, 'tags': tags})

      self.assertEqual(status, 1)
      self.assertIsNone(res)
    except Exception as e:
      print e
      raise 


  def test_delete_paper_valid(self):
    try:
      pid = 1
      status, res = db_wrapper_debug(funcs.delete_paper, {'pid': pid})

      self.assertEqual(status, SUCCESS)
      self.assertIsNone(res)
    except Exception as e:
      print e
      raise 


  def test_delete_paper_invalid_pid(self):
    try:
      # sort of a hoaky test, but if there's nothing to delete, nothing bad happens, so success
      pid = 100
      status, res = db_wrapper_debug(funcs.delete_paper, {'pid': pid})

      self.assertEqual(status, SUCCESS)
      self.assertIsNone(res)
    except Exception as e:
      print e
      raise 

  
  def test_get_paper_tags_valid(self):
    try:
      pid = 1
      status, res = db_wrapper_debug(funcs.get_paper_tags, {'pid': pid})
     
      self.assertEqual(status, SUCCESS)
      self.assertEqual(res, [TAGS[0], TAGS[1]])
    except Exception as e:
      print e
      raise 


  def test_get_paper_tags_invalid_pid(self):
    try:
      pid = 100
      status, res = db_wrapper_debug(funcs.get_paper_tags, {'pid': pid})
    
      self.assertEqual(status, SUCCESS)
      self.assertEqual(res, [])
    except Exception as e:
      print e
      raise 


  def test_like_paper_valid(self):
    try:
      pid = 1
      user = USERS[3]
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': pid, 'uname': user})

      self.assertEqual(status, SUCCESS)
      self.assertIsNone(res)

    except Exception as e:
      print e
      raise 


  def test_like_paper_author_is_user(self):
    try:
      pid = 1
      user = USERS[0]
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': pid, 'uname': user})

      self.assertEqual(status, 1)
      self.assertIsNone(res)

    except Exception as e:
      print e
      raise 


  def test_like_paper_user_already_liked(self):
    try:
      pid = 1
      user = USERS[3]
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': pid, 'uname': user})

      self.assertEqual(status, SUCCESS)
      self.assertIsNone(res)

      status, res = db_wrapper_debug(funcs.like_paper, {'pid': pid, 'uname': user})
     
      # this call to like should fail because they've already liked the paper
      self.assertEqual(status, 1)
      self.assertIsNone(res)

    except Exception as e:
      print e     
      raise 


  def test_like_paper_invalid_pid(self):
    try:
      pid = 100
      user = USERS[2]
      # this causes a foreign key constraint error
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': pid, 'uname': user})

      self.assertEqual(status, 1)
      self.assertIsNone(res)
    except Exception as e:
      print e
      raise 

  
  def test_unlike_paper_valid(self):
    try:
      pid = 1
      user = USERS[2]
 
      # like followed by unlike
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': pid, 'uname': user})
      status, res = db_wrapper_debug(funcs.unlike_paper, {'pid': pid, 'uname': user})
      
      self.assertEqual(status, SUCCESS)
      self.assertIsNone(res)

    except Exception as e:
      print e
      raise 

  
  def test_unlike_paper_user_has_not_liked(self):
    try:
      pid = 1
      user = USERS[2]

      status, res = db_wrapper_debug(funcs.unlike_paper, {'pid': pid, 'uname': user})
      
      self.assertEqual(status, 1)
      self.assertIsNone(res)

    except Exception as e:
      print e
      raise 


  def test_unlike_paper_invalid_pid(self):
    try:
      pid = 100
      user = USERS[2]

      status, res = db_wrapper_debug(funcs.unlike_paper, {'pid': pid, 'uname': user})

      self.assertEqual(status, 1)
      self.assertIsNone(res)

    except Exception as e:
      print e
      raise 


  def test_get_likes_valid(self):
    try:
      pid = 1
      
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': pid, 'uname': USERS[1]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': pid, 'uname': USERS[2]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': pid, 'uname': USERS[3]})

      status, res = db_wrapper_debug(funcs.get_likes, {'pid': pid})
      
      self.assertEqual(status, SUCCESS)
      self.assertEqual(res, 3)

    except Exception as e:
      print e
      raise 


  def test_get_likes_invalid_pid(self):
    try:
      pid = 100

      status, res = db_wrapper_debug(funcs.get_likes, {'pid': pid})
      
      self.assertEqual(status, SUCCESS)
      self.assertEqual(res, 0)

    except Exception as e:
      print e
      raise 


  def test_get_timeline_valid(self):
    try:
      user = USERS[0]
      status, res = db_wrapper_debug(funcs.get_timeline, {'uname': user})

      self.assertEqual(status, SUCCESS)
    
      self.assertEqual(res[0][1], user)
      self.assertEqual(res[0][2], TITLES[1])
      self.assertEqual(res[0][4], DESCS[1])

      self.assertEqual(res[1][1], user)
      self.assertEqual(res[1][2], TITLES[0])
      self.assertEqual(res[1][4], DESCS[0])
 
    except Exception as e:
      print e
      raise 

 
  def test_get_timeline_smaller_count_than_papers(self):
    try:
      user = USERS[0]
      count = 1

      status, res = db_wrapper_debug(funcs.get_timeline, {'uname': user, 'count': count})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 1)
    
      self.assertEqual(res[0][1], user)
      self.assertEqual(res[0][2], TITLES[1])
      self.assertEqual(res[0][4], DESCS[1])
      
    except Exception as e:
      print e
      raise 
  
 
  def test_get_timeline_larger_count_than_papers(self):
    try:
      user = USERS[0]
      count = 5

      status, res = db_wrapper_debug(funcs.get_timeline, {'uname': user, 'count': count})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 2)
    
      self.assertEqual(res[0][1], user)
      self.assertEqual(res[0][2], TITLES[1])
      self.assertEqual(res[0][4], DESCS[1])

      self.assertEqual(res[1][1], user)
      self.assertEqual(res[1][2], TITLES[0])
      self.assertEqual(res[1][4], DESCS[0])
      
    except Exception as e:
      print e
      raise 
   


  def test_get_timeline_all_valid(self):
    try:
      status, res = db_wrapper_debug(funcs.get_timeline_all, {'count': 4})
      
      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), len(TITLES))

    except Exception as e:
      print e
      raise 


  def test_get_timeline_all_smaller_count_than_papers(self):
    try:
      status, res = db_wrapper_debug(funcs.get_timeline_all, {'count': 2})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 2)

    except Exception as e:
      print e
      raise 
  

  def test_get_timeline_all_larger_count_than_papers(self):
    try:
      status, res = db_wrapper_debug(funcs.get_timeline_all, {'count': 10})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 4)

    except Exception as e:
      print e
      raise 


 
  def test_get_most_popular_papers_valid(self):
    try:
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 1, 'uname': USERS[4]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 2, 'uname': USERS[4]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 3, 'uname': USERS[2]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 4, 'uname': USERS[1]})

      status, res = db_wrapper_debug(funcs.get_most_popular_papers, {'count': 4, 'begin_time':datetime.now() + timedelta(days=-1)})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 4)

      begin_time = datetime.now()
      status, res = db_wrapper_debug(funcs.get_most_popular_papers, {'begin_time':datetime.now()})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(res, [])

    except Exception as e:
      print e
      raise 


  def test_get_most_popular_papers_smaller_count_than_papers(self): 
    try:
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 1, 'uname': USERS[4]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 2, 'uname': USERS[4]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 3, 'uname': USERS[2]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 4, 'uname': USERS[1]})

      status, res = db_wrapper_debug(funcs.get_most_popular_papers, {'count': 2, 'begin_time':datetime.now() + timedelta(days=-1)})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 2)
      self.assertEqual(res[0][0], 1)
      self.assertEqual(res[1][0], 2)

      begin_time = datetime.now()
      status, res = db_wrapper_debug(funcs.get_most_popular_papers, {'begin_time':datetime.now()})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(res, [])

    except Exception as e:
      print e
      raise 


  def test_get_most_popular_papers_larger_count_than_papers(self):
    try:
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 1, 'uname': USERS[4]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 2, 'uname': USERS[4]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 3, 'uname': USERS[2]})
      status, res = db_wrapper_debug(funcs.like_paper, {'pid': 4, 'uname': USERS[1]})

      status, res = db_wrapper_debug(funcs.get_most_popular_papers, {'count': 10, 'begin_time':datetime.now() + timedelta(days=-1)})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 4)
      self.assertEqual(res[0][0], 1)
      self.assertEqual(res[1][0], 2)

      begin_time = datetime.now()
      status, res = db_wrapper_debug(funcs.get_most_popular_papers, {'begin_time':datetime.now()})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(res, [])

    except Exception as e:
      print e
      raise 


  def test_get_recommend_papers_valid(self):
    try:
      for likes in [[1, 1], [2, 1], [2, 2], [2, 3], [3, 1], [3, 3]]:
        status, res = db_wrapper_debug(funcs.like_paper, {'uname':USERS[likes[0]], 'pid':likes[1]})

      status, res = db_wrapper_debug(funcs.get_recommend_papers, {'uname': USERS[1]})
      
      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 1)
      self.assertEqual(res[0][0], 2)

    except Exception as e:
      print e
      raise 


  def test_get_recommend_papers_no_recommendations(self):
    try:
      for likes in [[1,1], [2,2], [3,3], [4,4]]:
        status, res = db_wrapper_debug(funcs.like_paper, {'uname':USERS[likes[0]], 'pid':likes[1]})

      status, res = db_wrapper_debug(funcs.get_recommend_papers, {'uname': USERS[1]})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(res, [])  
 
    except Exception as e:
      print e
      raise 


  def test_get_papers_by_tag_valid(self):
    try:
      status, res = db_wrapper_debug(funcs.get_papers_by_tag, {'tag': TAGS[0]})
      
      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 3)

    except Exception as e:
      print e
      raise 

 
  def test_get_papers_by_tag_tag_nonexistent(self):
    try:
      status, res = db_wrapper_debug(funcs.get_papers_by_tag, {'tag': 'chicken'})
      
      self.assertEqual(status, SUCCESS)
      self.assertEqual(res, [])

    except Exception as e:
      print e
      raise 



  def test_get_papers_by_keyword_valid(self):
    try:
      status, res = db_wrapper_debug(funcs.get_papers_by_keyword, {'keywords': 'oldest'})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 1)
      self.assertEqual(res[0][0], 1)

      status, res = db_wrapper_debug(funcs.get_papers_by_keyword, {'keywords': 'description'})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 4)  # all the papers

    except Exception as e:
      print e
      raise 


  def test_get_papers_by_keyword_keyword_not_found(self):
    try:
      status, res = db_wrapper_debug(funcs.get_papers_by_keyword, {'keywords': 'databases'})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 0)

      status, res = db_wrapper_debug(funcs.get_papers_by_keyword, {'keywords': 'ASDFJ'})

      self.assertEqual(status, SUCCESS)
      self.assertEqual(len(res), 0)

    except Exception as e:
      print e
      raise 


  def test_get_papers_by_liked_valid(self):
    try:
      raise ValueError
    except Exception as e:
      print e
      raise 

  def test_get_most_active_users_valid(self):
    pass
  

  def test_get_most_popular_tags_valid(self):
    pass


  def test_get_most_popular_tag_pairs_valid(self):
    pass


  def test_get_number_papers_user_valid(self):
    pass


  def test_get_number_papers_user_nonexistent(self):
    pass


  def test_get_number_liked_user_valid(self):
    pass

 
  def test_get_number_liked_user_nonexistent(self):
    pass


  def test_get_number_tags_user_valid(self):
    pass

  
  def test_get_number_tags_user_nonexistent(self):
    pass


suite_all = unittest.TestLoader().loadTestsFromTestCase(TestFuncMethods)
unittest.TextTestRunner(verbosity = 2).run(suite_all)
