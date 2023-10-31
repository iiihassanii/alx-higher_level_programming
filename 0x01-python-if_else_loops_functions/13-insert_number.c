#include "list.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *insert, node = *head;

	insert->n = number;

	if(!head || *head)
		return (NULL);
	while (node)
	{
		if(number > node->n)
		{
			if(!node->next)
			{
				node->next = insert;
				return (insert);
			}
			else if (node->next->n < number)
			{
				insert->next = node->next;
				node->next = insert;
				return (insert);
			}
		}
		node = node->next;
	}
	return (NULL);
}
