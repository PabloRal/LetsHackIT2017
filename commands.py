import functools
from comp.comp_register import comp_register
from comp.comp_list import comp_list
from comp.comp_add_task import comp_add_task
from comp.comp_tasks_list import comp_tasks_list
from comp.comp_join import user_comps_register
from comp.comp_submit_anwer import comp_submit_answer
from comp.my_comps import show_my_comps
from comp.comp_contestants import comp_contestants
from comp.comp_answers_ranking import answers_ranking_parse

def get_commands(redis_client):
    return {
        'comp_register': functools.partial(comp_register, redis_client),
        'comp_list': functools.partial(comp_list, redis_client),
        'comp_tasks_list': functools.partial(comp_tasks_list, redis_client),
        'comp_add_task': functools.partial(comp_add_task, redis_client),
        'comp_submit_answer': functools.partial(comp_submit_answer, redis_client),
        'show_my_comps' : functools.partial(show_my_comps, redis_client),
        'comp_join': functools.partial(user_comps_register, redis_client),
        'comp_contestants': functools.partial(comp_contestants, redis_client),
        'answers_ranking': functools.partial(answers_ranking_parse, redis_client)
    }