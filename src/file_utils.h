#ifndef FILE_UTILS_H
#define FILE_UTILS_H

int is_dir(const char *path);

int is_file(const char *path);

void remove_newline_chars(char *str);

int truncate_file(const char *path);

#endif

#ifndef PATH_MAX_SIZE
#define PATH_MAX_SIZE 4096
#endif