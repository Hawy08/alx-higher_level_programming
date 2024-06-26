#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - check cycle in a cycle
 * Return: true if there is a loop in linked list else  false.
 */

int check_cycle(listint_t *list)
{
    listint_t *current, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	check = current->next;

	while (current != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}
