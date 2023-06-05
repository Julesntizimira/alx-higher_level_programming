# include "lists.h"
/**
 * check_cycle - function to chech if there is a cycle in list
 * @list: input list
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;

	while (fast && slow && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
