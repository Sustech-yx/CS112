dictionary = dict()
filepath = input()
sp_name = input()

dictionary['.'] = [
    'README.txt',
    {
        'bin': ['run_tests']
    },
    {
        'py_trace_event': [
            'setup.py', 'trace_event.py', 'trace_event_unittest.py',
            'trace_time.py', 'trace_time_unittest.py', '__init__.py',
            {
                'trace_event_impl': [
                    'decorators.py',
                    'decorators_test.py',
                    'log.py',
                    'log_io_test.py',
                    'meta_class.py',
                    'multiprocessing_shim.py',
                    'parsed_trace_events.py',
                    'perfetto_proto_classes.py',
                    'perfetto_trace_writer.py',
                    'perfetto_trace_writer_unittest.py',
                    'trace_test.py',
                    '__init__.py'
                ]
            }
        ]
    }, {
        'third_party': [
            {'protobuf': [
                'encoder.py',
                'README.chromium',
                'wire_format.py'
            ]}
        ]
    }]

# walking = filepath.split('/')
# for walk in walking:
#     if type(dictionary) is dict:
#         dictionary = dictionary[walk]
#     else:
#         for element in dictionary:
#             if type(element) == dict:
#                 if walk in element.keys():
#                     dictionary = element[walk]
#                     break

if 'bin' in filepath:
    dictionary = dictionary['.'][1]['bin']
elif 'py' in filepath:
    dictionary = dictionary['.'][2]['py_trace_event']
elif 'impl' in filepath:
    dictionary = dictionary['.'][2]['py_trace_event'][6]['trace_event_impl']
elif 'third_party' in filepath:
    dictionary = dictionary['.'][3]['third_party']
elif 'pro' in filepath:
    dictionary = dictionary['.'][3]['third_party'][0]['protobuf']
else:
    dictionary = dictionary['.']
res = []
for element in dictionary:
    if type(element) == str:
        if sp_name in element:
            res.append(element)

res = sorted(res)
print('\n'.join(res))