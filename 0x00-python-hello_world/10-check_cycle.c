#include "lists.h"

/**
 * check_cycle - function checks cycle
 * @list: pointer to the node
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *node = list, *nnode = list;

	while (nnode && nnode->next)
	{
		node = node->next;
		nnode = nnode->next->next;
		if (node == nnode)
                        return (1);
	}
	return (0);
}
