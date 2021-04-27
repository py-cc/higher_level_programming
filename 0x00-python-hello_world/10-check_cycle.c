#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to head
 * 
 * Return: 0 if there is no cycle, 1 if there is a cycle
 *
 */
int check_cycle(listint_t *list)
{
	const listint_t *node_1 = list;
	const listint_t *node_2 = list;

	while (node_2)
	{
		node_1 = node_1->next;
		node_2 = node_2->next->next;
		if (node_1 == node_2)
			return (1);	
	}
	return (0);
}
