#include <Python.h>

#ifndef TYK_COPROCESS_PYTHON_DISPATCHER
#define TYK_COPROCESS_PYTHON_DISPATCHER

extern void dispatch_hook(char*, char*);

static char* dispatcher_module_name = "dispatcher";
static char* dispatcher_class_name = "TykDispatcher";
static char* hook_name = "dispatch_hook";

static PyObject* dispatcher_module;
static PyObject* dispatcher_module_dict;
static PyObject* dispatcher_class;

static PyObject* dispatcher_args;
static PyObject* dispatcher;

static PyObject* dispatcher_hook_name;
static PyObject* dispatcher_hook;

static char* dispatcher_reload = "reload";
static PyObject* dispatcher_reload_hook;

#endif
