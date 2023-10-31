#include "lists.h"
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert, *node = *head;

	insert = malloc(sizeof(listint_t));
	insert->n = number;

	if(!head || !*head)
	{
		*head = insert;
		return (insert);
	}
	while (node)
	{
		if(number >= node->n)
		{
			if(!node->next)
			{
				node->next = insert;
				insert->next = NULL;
				return (insert);
			}
			else if (node->next->n >= number)
			{
				insert->next = node->next;
				node->next = insert;
				return (insert);
			}
		}
		else
		{
			insert->next = node;
			*head = insert;
			return (insert);
		}
		node = node->next;
	}
	return (NULL);
}
