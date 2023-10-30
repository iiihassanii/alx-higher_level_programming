#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - function checks cycle
 * @list: beginning of the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *node, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	node = list;
	check = node->next;

	while (check != NULL)
	{
		if (node == check)
			return (1);
		node = check;
		check = node->next;
	}
	return (0);
}
